import { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import axios from 'axios'
import ScoreBars from '../components/ScoreBars'

export default function GameSession() {
  const { sessionId } = useParams()
  const navigate = useNavigate()
  const [session, setSession] = useState(null)
  const [actions, setActions] = useState([])
  const [actionLibrary, setActionLibrary] = useState([])
  const [selectedAction, setSelectedAction] = useState(null)
  const [customAction, setCustomAction] = useState('')
  const [customUserMovement, setCustomUserMovement] = useState(0)
  const [customLlmMovement, setCustomLlmMovement] = useState(0)
  const [loading, setLoading] = useState(true)
  const [showCustom, setShowCustom] = useState(false)
  const [trackedActions, setTrackedActions] = useState([])
  const [selectedActionIds, setSelectedActionIds] = useState([])

  useEffect(() => {
    fetchSession()
    fetchActionLibrary()
    fetchTrackedActions()
    fetchSelectedActions()
  }, [sessionId])

  const fetchSession = async () => {
    try {
      const response = await axios.get(`/api/sessions/${sessionId}`)
      setSession(response.data)
    } catch (error) {
      console.error('Failed to fetch session:', error)
      navigate('/dashboard')
    } finally {
      setLoading(false)
    }
  }

  const fetchActionLibrary = async () => {
    try {
      const response = await axios.get('/api/actions/library')
      setActionLibrary(response.data)
    } catch (error) {
      console.error('Failed to fetch action library:', error)
    }
  }

  const fetchTrackedActions = async () => {
    try {
      const response = await axios.get(`/api/actions/session/${sessionId}/actions`)
      setTrackedActions(response.data)
    } catch (error) {
      console.error('Failed to fetch tracked actions:', error)
    }
  }

  const fetchSelectedActions = async () => {
    try {
      const response = await axios.get(`/api/sessions/${sessionId}/selected-actions`)
      setSelectedActionIds(response.data)
    } catch (error) {
      console.error('Failed to fetch selected actions:', error)
    }
  }

  const trackAction = async (libraryId = null, description = null, userMov = 0, llmMov = 0) => {
    try {
      const response = await axios.post('/api/actions/track', {
        session_id: parseInt(sessionId),
        library_id: libraryId,
        action_description: description,
        user_movement: userMov,
        llm_movement: llmMov
      })

      // Update local session scores immediately for smooth UX
      setSession(prev => ({
        ...prev,
        user_score: prev.user_score + userMov,
        llm_score: prev.llm_score + llmMov
      }))

      setActions(prev => [response.data, ...prev])
      setSelectedAction(null)
      setShowCustom(false)
      setCustomAction('')

      // Refresh tracked actions
      fetchTrackedActions()
    } catch (error) {
      console.error('Failed to track action:', error)
      alert('Failed to track action')
    }
  }

  const handleLibraryAction = (action) => {
    trackAction(
      action.library_id,
      null,
      action.default_user_movement,
      action.default_llm_movement
    )
  }

  const handleCustomAction = (e) => {
    e.preventDefault()
    if (!customAction.trim()) return

    trackAction(
      null,
      customAction,
      parseInt(customUserMovement),
      parseInt(customLlmMovement)
    )
  }

  const pauseSession = async () => {
    try {
      const response = await axios.post(`/api/sessions/${sessionId}/pause`)
      setSession(response.data)
    } catch (error) {
      console.error('Failed to pause session:', error)
    }
  }

  const resumeSession = async () => {
    try {
      const response = await axios.post(`/api/sessions/${sessionId}/resume`)
      setSession(response.data)
    } catch (error) {
      console.error('Failed to resume session:', error)
    }
  }

  const endSession = async () => {
    if (!confirm('Are you sure you want to end this session?')) return

    try {
      await axios.post(`/api/sessions/${sessionId}/end`)
      navigate('/dashboard')
    } catch (error) {
      console.error('Failed to end session:', error)
    }
  }

  if (loading) {
    return <div className="flex items-center justify-center min-h-screen">Loading...</div>
  }

  if (!session) {
    return null
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm sticky top-0 z-10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center justify-between">
            <button
              onClick={() => navigate('/dashboard')}
              className="text-gray-600 hover:text-gray-900"
            >
              ← Back to Dashboard
            </button>
            <h1 className="text-xl font-bold text-gray-900">
              {session.session_name || `Session ${session.session_id}`}
            </h1>
            <div className="flex gap-2">
              {session.status === 'active' && (
                <>
                  <button
                    onClick={pauseSession}
                    className="px-4 py-2 text-sm bg-yellow-500 text-white rounded-md hover:bg-yellow-600"
                  >
                    Pause
                  </button>
                  <button
                    onClick={endSession}
                    className="px-4 py-2 text-sm bg-red-500 text-white rounded-md hover:bg-red-600"
                  >
                    End Session
                  </button>
                </>
              )}
              {session.status === 'paused' && (
                <button
                  onClick={resumeSession}
                  className="px-4 py-2 text-sm bg-green-500 text-white rounded-md hover:bg-green-600"
                >
                  Resume
                </button>
              )}
            </div>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Score Bars - Sticky */}
        <div className="sticky top-16 z-20 bg-white rounded-lg shadow p-6 mb-8">
          <h2 className="text-lg font-semibold mb-4">Collaboration Balance</h2>
          <ScoreBars userScore={session.user_score} llmScore={session.llm_score} />
        </div>

        {session.status === 'active' && (
          <>
            {/* Quick Actions */}
            <div className="bg-white rounded-lg shadow p-6 mb-8">
              <div className="flex justify-between items-center mb-4">
                <h2 className="text-lg font-semibold">Quick Actions</h2>
                <button
                  onClick={() => setShowCustom(!showCustom)}
                  className="text-sm text-user-color hover:text-blue-700 font-medium"
                >
                  {showCustom ? 'Show Library' : 'Custom Action'}
                </button>
              </div>

              {showCustom ? (
                <form onSubmit={handleCustomAction} className="space-y-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">
                      Action Description
                    </label>
                    <input
                      type="text"
                      value={customAction}
                      onChange={(e) => setCustomAction(e.target.value)}
                      placeholder="What did you do?"
                      required
                      className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-user-color"
                    />
                  </div>
                  <div className="grid grid-cols-2 gap-4">
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2">
                        Your Points
                      </label>
                      <input
                        type="number"
                        value={customUserMovement}
                        onChange={(e) => setCustomUserMovement(e.target.value)}
                        placeholder="0"
                        className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-user-color"
                      />
                    </div>
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2">
                        LLM Points
                      </label>
                      <input
                        type="number"
                        value={customLlmMovement}
                        onChange={(e) => setCustomLlmMovement(e.target.value)}
                        placeholder="0"
                        className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-user-color"
                      />
                    </div>
                  </div>
                  <button
                    type="submit"
                    className="w-full px-4 py-2 bg-user-color text-white rounded-md hover:bg-blue-700"
                  >
                    Track Custom Action
                  </button>
                </form>
              ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                  {actionLibrary
                    .filter(action => selectedActionIds.length === 0 || selectedActionIds.includes(action.library_id))
                    .map((action) => (
                    <button
                      key={action.library_id}
                      onClick={() => handleLibraryAction(action)}
                      className="text-left p-4 border-2 border-gray-200 rounded-lg hover:border-user-color hover:bg-blue-50 transition group"
                    >
                      <p className="text-sm font-medium text-gray-900 group-hover:text-user-color">
                        {action.action_description}
                      </p>
                      <div className="flex gap-4 mt-2 text-xs text-gray-600">
                        <span className="text-user-color">You: {action.default_user_movement > 0 ? '+' : ''}{action.default_user_movement}</span>
                        <span className="text-llm-color">LLM: {action.default_llm_movement > 0 ? '+' : ''}{action.default_llm_movement}</span>
                        <span className="ml-auto">Used {action.times_used}x</span>
                      </div>
                    </button>
                  ))}
                </div>
              )}
            </div>
          </>
        )}

        {session.status === 'paused' && (
          <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-6 mb-8 text-center">
            <p className="text-yellow-800">Session is paused. Resume to continue tracking.</p>
          </div>
        )}

        {session.status === 'ended' && (
          <div className="bg-gray-50 border border-gray-200 rounded-lg p-6 mb-8 text-center">
            <p className="text-gray-800">This session has ended.</p>
          </div>
        )}

        {/* Session History */}
        {trackedActions.length > 0 && (
          <div className="bg-white rounded-lg shadow p-6">
            <h2 className="text-lg font-semibold mb-4">Session History</h2>
            <div className="space-y-3">
              {trackedActions.map((action, index) => {
                // Find the library action for description if library_id exists
                const libraryAction = action.library_id
                  ? actionLibrary.find(a => a.library_id === action.library_id)
                  : null
                const description = libraryAction?.action_description || action.action_description || 'Custom action'

                return (
                  <div key={action.action_id} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                    <div className="flex items-center gap-3">
                      <span className="text-sm font-medium text-gray-500">#{trackedActions.length - index}</span>
                      <span className="text-sm text-gray-900">{description}</span>
                    </div>
                    <div className="flex gap-4 text-xs">
                      <span className={`font-medium ${action.user_movement > 0 ? 'text-user-color' : action.user_movement < 0 ? 'text-red-600' : 'text-gray-500'}`}>
                        You: {action.user_movement > 0 ? '+' : ''}{action.user_movement}
                      </span>
                      <span className={`font-medium ${action.llm_movement > 0 ? 'text-llm-color' : action.llm_movement < 0 ? 'text-red-600' : 'text-gray-500'}`}>
                        LLM: {action.llm_movement > 0 ? '+' : ''}{action.llm_movement}
                      </span>
                    </div>
                  </div>
                )
              })}
            </div>
          </div>
        )}
      </main>
    </div>
  )
}
