"""
Seed the database with starter action library.
Run this script after the database is created.
"""
from app.database import SessionLocal
from app.models import ActionLibrary

def seed_action_library():
    db = SessionLocal()

    # Check if actions already exist
    existing_count = db.query(ActionLibrary).filter(ActionLibrary.user_created == False).count()
    if existing_count > 0:
        print(f"Found {existing_count} existing starter actions. Skipping seed.")
        db.close()
        return

    # Starter actions for the game
    # user_movement: positive = user gains control, negative = user loses control
    # llm_movement: positive = LLM gains control, negative = LLM loses control

    starter_actions = [
        # Human Advance (Net > +2)
        {
            "action_description": "Pushed back on AI's suggestion and steered new direction",
            "default_user_movement": 4,
            "default_llm_movement": -1,
            "user_created": False
        },
        {
            "action_description": "Attempted my own explanation of a concept before asking AI",
            "default_user_movement": 3,
            "default_llm_movement": 0,
            "user_created": False
        },
        {
            "action_description": "Fact-checked AI's response before using it",
            "default_user_movement": 3,
            "default_llm_movement": 0,
            "user_created": False
        },
        {
            "action_description": "Created a draft myself first, then asked AI to review",
            "default_user_movement": 4,
            "default_llm_movement": 0,
            "user_created": False
        },

        # Balanced (Net -2 to +2)
        {
            "action_description": "Put AI's explanation into my own words",
            "default_user_movement": 2,
            "default_llm_movement": 0,
            "user_created": False
        },
        {
            "action_description": "Asked a specific follow-up question to understand better",
            "default_user_movement": 2,
            "default_llm_movement": 1,
            "user_created": False
        },
        {
            "action_description": "Asked AI to critique my work",
            "default_user_movement": 2,
            "default_llm_movement": 1,
            "user_created": False
        },
        {
            "action_description": "Asked AI to quiz me on what I'm learning",
            "default_user_movement": 2,
            "default_llm_movement": 1,
            "user_created": False
        },
        {
            "action_description": "Worked with AI to learn a new concept",
            "default_user_movement": 2,
            "default_llm_movement": 1,
            "user_created": False
        },
        {
            "action_description": "Used AI-generated outline as starting point, then adapted",
            "default_user_movement": 1,
            "default_llm_movement": 2,
            "user_created": False
        },

        # AI Advance (Net < -2)
        {
            "action_description": "Asked AI to summarize a long document",
            "default_user_movement": -1,
            "default_llm_movement": 2,
            "user_created": False
        },
        {
            "action_description": "Asked AI to write something from scratch for me",
            "default_user_movement": -2,
            "default_llm_movement": 3,
            "user_created": False
        },
        {
            "action_description": "Used AI's output without verifying accuracy",
            "default_user_movement": -3,
            "default_llm_movement": 4,
            "user_created": False
        },
        {
            "action_description": "Copy-pasted AI response without reading it",
            "default_user_movement": -3,
            "default_llm_movement": 4,
            "user_created": False
        },
    ]

    for action_data in starter_actions:
        action = ActionLibrary(**action_data)
        db.add(action)

    db.commit()
    print(f"✅ Seeded {len(starter_actions)} starter actions!")
    db.close()

if __name__ == "__main__":
    seed_action_library()
