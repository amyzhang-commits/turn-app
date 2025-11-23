export default function ScoreBars({ userScore, llmScore }) {
  const total = Math.max(userScore + llmScore, 1) // Avoid division by zero
  const userPercent = (userScore / total) * 100
  const llmPercent = (llmScore / total) * 100

  return (
    <div className="w-full space-y-4">
      {/* User Bar */}
      <div>
        <div className="flex justify-between mb-2">
          <span className="text-sm font-medium text-gray-700">You</span>
          <span className="text-sm font-bold text-user-color">{userScore}</span>
        </div>
        <div className="w-full bg-gray-200 rounded-full h-8 overflow-hidden">
          <div
            className="bg-user-color h-8 rounded-full transition-all duration-500 ease-out flex items-center justify-end px-3"
            style={{ width: `${userPercent}%` }}
          >
            {userScore > 0 && (
              <span className="text-white text-xs font-bold">{Math.round(userPercent)}%</span>
            )}
          </div>
        </div>
      </div>

      {/* LLM Bar */}
      <div>
        <div className="flex justify-between mb-2">
          <span className="text-sm font-medium text-gray-700">LLM</span>
          <span className="text-sm font-bold text-llm-color">{llmScore}</span>
        </div>
        <div className="w-full bg-gray-200 rounded-full h-8 overflow-hidden">
          <div
            className="bg-llm-color h-8 rounded-full transition-all duration-500 ease-out flex items-center justify-end px-3"
            style={{ width: `${llmPercent}%` }}
          >
            {llmScore > 0 && (
              <span className="text-white text-xs font-bold">{Math.round(llmPercent)}%</span>
            )}
          </div>
        </div>
      </div>

      {/* Balance Indicator */}
      <div className="text-center text-sm text-gray-600 mt-2">
        {userScore > llmScore && "You're leading!"}
        {llmScore > userScore && "LLM is leading!"}
        {userScore === llmScore && userScore === 0 && "Start tracking to see your balance"}
        {userScore === llmScore && userScore > 0 && "Perfect balance!"}
      </div>
    </div>
  )
}
