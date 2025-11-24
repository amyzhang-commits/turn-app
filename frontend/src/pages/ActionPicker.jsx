import { useState, useEffect } from 'react'
import { useNavigate, useLocation } from 'react-router-dom'
import axios from 'axios'

export default function ActionPicker() {
  const navigate = useNavigate()
  const location = useLocation()
  const sessionName = location.state?.sessionName || ''

  const [actionLibrary, setActionLibrary] = useState([])
  const [selectedActions, setSelectedActions] = useState([])
  const [loading, setLoading] = useState(true)
  const [creating, setCreating] = useState(false)

  useEffect(() => {
    fetchActionLibrary()
  }, [])

  const fetchActionLibrary = async () => {
    try {
      const response = await axios.get('/api/actions/library')
      setActionLibrary(response.data)
    } catch (error) {
      console.error('Failed to fetch action library:', error)
    } finally {
      setLoading(false)
    }
  }

  const toggleAction = (libraryId) => {
    if (selectedActions.includes(libraryId)) {
      setSelectedActions(selectedActions.filter(id => id !== libraryId))
    } else {
      if (selectedActions.length < 7) {
        setSelectedActions([...selectedActions, libraryId])
      }
    }
  }

  const createSession = async () => {
    if (selectedActions.length < 3) {
      alert('Please select at least 3 actions to track')
      return
    }

    setCreating(true)
    try {
      const response = await axios.post('/api/sessions/', {
        session_name: sessionName || null
      }, {
        params: {
          selected_action_ids: selectedActions
        }
      })
      navigate(`/session/${response.data.session_id}`)
    } catch (error) {
      console.error('Failed to create session:', error)
      alert('Failed to create session')
    } finally {
      setCreating(false)
    }
  }

  if (loading) {
    return <div className="flex items-center justify-center min-h-screen">Loading...</div>
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex justify-between items-center">
          <button
            onClick={() => navigate('/dashboard')}
            className="text-gray-600 hover:text-gray-900"
          >
            ← Cancel
          </button>
          <h1 className="text-xl font-bold text-gray-900">Select Actions to Track</h1>
          <div className="w-16"></div>
        </div>
      </header>

      <main className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Instructions */}
        <div className="bg-blue-50 border border-blue-200 rounded-lg p-6 mb-8">
          <h2 className="text-lg font-semibold text-blue-900 mb-2">
            Pick 3-7 actions for this session
          </h2>
          <p className="text-sm text-blue-800">
            Choose the actions you're most likely to do during this work session. This keeps tracking quick and focused!
          </p>
          <p className="text-sm text-blue-700 mt-2">
            Selected: {selectedActions.length} / 7 {selectedActions.length >= 3 && '✓'}
          </p>
        </div>

        {/* Action Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8">
          {actionLibrary.map((action) => {
            const isSelected = selectedActions.includes(action.library_id)
            const isDisabled = !isSelected && selectedActions.length >= 7

            return (
              <button
                key={action.library_id}
                onClick={() => toggleAction(action.library_id)}
                disabled={isDisabled}
                className={`text-left p-4 border-2 rounded-lg transition ${
                  isSelected
                    ? 'border-user-color bg-blue-50'
                    : isDisabled
                    ? 'border-gray-200 bg-gray-100 opacity-50 cursor-not-allowed'
                    : 'border-gray-200 hover:border-user-color hover:bg-blue-50'
                }`}
              >
                <div className="flex items-start gap-3">
                  <div className={`mt-1 w-5 h-5 rounded border-2 flex items-center justify-center ${
                    isSelected ? 'bg-user-color border-user-color' : 'border-gray-300'
                  }`}>
                    {isSelected && (
                      <svg className="w-3 h-3 text-white" fill="currentColor" viewBox="0 0 20 20">
                        <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                      </svg>
                    )}
                  </div>
                  <div className="flex-1">
                    <p className="text-sm font-medium text-gray-900">
                      {action.action_description}
                    </p>
                    <div className="flex gap-4 mt-2 text-xs text-gray-600">
                      <span className="text-user-color">
                        You: {action.default_user_movement > 0 ? '+' : ''}{action.default_user_movement}
                      </span>
                      <span className="text-llm-color">
                        LLM: {action.default_llm_movement > 0 ? '+' : ''}{action.default_llm_movement}
                      </span>
                    </div>
                  </div>
                </div>
              </button>
            )
          })}
        </div>

        {/* Start Button */}
        <div className="sticky bottom-0 bg-white border-t border-gray-200 p-4 -mx-4">
          <div className="max-w-4xl mx-auto flex justify-between items-center">
            <p className="text-sm text-gray-600">
              {selectedActions.length < 3 && `Select at least ${3 - selectedActions.length} more action${3 - selectedActions.length === 1 ? '' : 's'}`}
              {selectedActions.length >= 3 && "You're all set!"}
            </p>
            <button
              onClick={createSession}
              disabled={selectedActions.length < 3 || creating}
              className="px-8 py-3 bg-user-color text-white rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-user-color disabled:opacity-50 disabled:cursor-not-allowed font-medium"
            >
              {creating ? 'Starting...' : 'Start Session'}
            </button>
          </div>
        </div>
      </main>
    </div>
  )
}
