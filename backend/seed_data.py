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
        {
            "action_description": "Asked LLM to explain code I wrote",
            "default_user_movement": 2,
            "default_llm_movement": 1,
            "user_created": False
        },
        {
            "action_description": "Asked LLM to write code from scratch",
            "default_user_movement": -2,
            "default_llm_movement": 3,
            "user_created": False
        },
        {
            "action_description": "Copy-pasted LLM code without reading",
            "default_user_movement": -3,
            "default_llm_movement": 4,
            "user_created": False
        },
        {
            "action_description": "Modified LLM's suggestion before using it",
            "default_user_movement": 3,
            "default_llm_movement": 1,
            "user_created": False
        },
        {
            "action_description": "Asked LLM to debug my code",
            "default_user_movement": 0,
            "default_llm_movement": 2,
            "user_created": False
        },
        {
            "action_description": "Rejected LLM's suggestion and wrote my own",
            "default_user_movement": 4,
            "default_llm_movement": -1,
            "user_created": False
        },
        {
            "action_description": "Asked LLM for ideas/brainstorming",
            "default_user_movement": 2,
            "default_llm_movement": 1,
            "user_created": False
        },
        {
            "action_description": "Used LLM to refactor code I understand",
            "default_user_movement": 1,
            "default_llm_movement": 2,
            "user_created": False
        },
        {
            "action_description": "Asked LLM to add a feature to existing code",
            "default_user_movement": -1,
            "default_llm_movement": 3,
            "user_created": False
        },
        {
            "action_description": "Read and understood LLM's explanation",
            "default_user_movement": 3,
            "default_llm_movement": 0,
            "user_created": False
        },
        {
            "action_description": "Asked follow-up questions to understand better",
            "default_user_movement": 3,
            "default_llm_movement": 0,
            "user_created": False
        },
        {
            "action_description": "Let LLM handle something I could do myself",
            "default_user_movement": -2,
            "default_llm_movement": 3,
            "user_created": False
        },
        {
            "action_description": "Wrote code myself first, then asked LLM to review",
            "default_user_movement": 4,
            "default_llm_movement": -1,
            "user_created": False
        },
        {
            "action_description": "Asked LLM to optimize my working code",
            "default_user_movement": 2,
            "default_llm_movement": 1,
            "user_created": False
        },
        {
            "action_description": "Used LLM to learn a new concept/library",
            "default_user_movement": 2,
            "default_llm_movement": 1,
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
