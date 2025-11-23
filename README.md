# Spade App

A gamified reflection support tool to help users be more mindful about their collaboration patterns with LLMs.

Track whether you're being more active or passive in your work with AI assistants. Visualize the balance between user control and LLM assistance through competing progress bars.

## Features

- **Real-time Score Tracking**: Two competing bars showing user vs LLM control
- **Quick Action Library**: Pre-populated common actions (copy-paste, asking for explanations, modifying suggestions, etc.)
- **Custom Actions**: Create your own actions with custom scoring
- **Session Management**: Start, pause, resume, and end game sessions
- **Multi-user Support**: Each user has their own sessions and custom actions
- **Mobile-First PWA**: Works on any device, can be added to home screen
- **Reflection Tool**: Review your collaboration patterns over time

## Tech Stack

**Backend:**
- FastAPI (Python)
- SQLAlchemy ORM
- PostgreSQL (production) / SQLite (development)
- JWT authentication

**Frontend:**
- React + Vite
- TailwindCSS
- React Router
- Axios

**Deployment:**
- Railway (hosting + PostgreSQL)
- PWA-ready for mobile devices

## Local Development Setup

### Prerequisites
- Python 3.11+
- Node.js 18+
- npm or yarn

### Backend Setup

1. Install Python dependencies:
```bash
pip install -e .
```

2. Create a `.env` file (copy from `.env.example`):
```bash
cp .env.example .env
```

For local development, the default SQLite database is fine. Edit `.env` if you want to use PostgreSQL locally.

3. Run the backend:
```bash
cd backend
python -m uvicorn app.main:app --reload --port 8000
```

4. Seed the database with starter actions:
```bash
cd backend
python seed_data.py
```

The API will be available at `http://localhost:8000`
- API docs: `http://localhost:8000/docs`
- Health check: `http://localhost:8000/health`

### Frontend Setup

1. Install dependencies:
```bash
cd frontend
npm install
```

2. Run the development server:
```bash
npm run dev
```

The app will be available at `http://localhost:3000`

## Railway Deployment

### Prerequisites
- Railway account (free tier works)
- GitHub repository

### Steps

1. **Push to GitHub:**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-repo-url>
git push -u origin main
```

2. **Create Railway Project:**
   - Go to [railway.app](https://railway.app)
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

3. **Add PostgreSQL Database:**
   - In your Railway project, click "New"
   - Select "Database" ’ "PostgreSQL"
   - Railway will automatically create a `DATABASE_URL` environment variable

4. **Configure Environment Variables:**
   - Go to your web service settings
   - Add these variables:
     - `SECRET_KEY`: Generate a secure random string
     - `DATABASE_URL`: Will be auto-populated by Railway
   - The `PORT` variable is automatically set by Railway

5. **Deploy:**
   - Railway will automatically deploy when you push to main
   - First deployment might take 3-5 minutes

6. **Run Database Seed:**
   After first deployment, seed the action library:
   - Go to Railway dashboard ’ your service ’ "Settings" ’ "Deploy"
   - Or SSH into the service and run: `python backend/seed_data.py`

7. **Get Your URL:**
   - Railway provides a URL like: `your-app.railway.app`
   - Share this with users!

### Post-Deployment

The app is now live and ready for users to:
1. Sign up for an account
2. Start a new session
3. Track their actions as they work with LLMs
4. See their collaboration balance in real-time

## Database Schema

Based on the ERD provided:

- **users**: User accounts with authentication
- **game_session**: Individual game sessions with scores
- **action_library**: Reusable actions (starter pack + user-created)
- **tracked_actions**: Actions taken during sessions
- **game_session_logs**: Timestamped log of all actions

## API Endpoints

### Authentication
- `POST /api/auth/signup` - Create account
- `POST /api/auth/login` - Login
- `GET /api/auth/me` - Get current user

### Sessions
- `POST /api/sessions/` - Create new session
- `GET /api/sessions/` - List user's sessions
- `GET /api/sessions/{id}` - Get session details
- `POST /api/sessions/{id}/pause` - Pause session
- `POST /api/sessions/{id}/resume` - Resume session
- `POST /api/sessions/{id}/end` - End session

### Actions
- `GET /api/actions/library` - Get action library
- `POST /api/actions/library` - Create custom action
- `POST /api/actions/track` - Track an action
- `GET /api/actions/session/{id}/actions` - Get session's actions

## Development Notes

### Scoring System

The scoring system uses two values for each action:
- **user_movement**: Points for user (positive = more control, negative = less)
- **llm_movement**: Points for LLM (positive = more control, negative = less)

Example actions:
- "Copy-pasted LLM code without reading": User -3, LLM +4
- "Modified LLM's suggestion before using": User +3, LLM +1
- "Rejected LLM's suggestion, wrote my own": User +4, LLM -1

### PWA Features

The app includes:
- Manifest file for "Add to Home Screen"
- Mobile-responsive design
- Offline-capable (can be extended with service workers)

### Future Enhancements

Potential additions:
- Session history view with charts
- Insights and patterns over time
- Rewards/badges system
- Export session data
- Collaborative sessions
- Browser extension integration

## License

MIT

## Contributing

This is a prototype/research tool. Contributions welcome!
