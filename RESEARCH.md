# 🔬 Turn: Research Methodology & Data Sharing

## Overview

Turn aims to build an **open, public dataset** of human-LLM collaboration patterns that anyone can use for research, teaching, or curiosity. Think of it as a "Kaggle dataset for AI collaboration ethnography."

This document outlines:
- What data we collect
- How privacy is protected
- How to contribute your data
- How to use the dataset for research or teaching
- Ethics and informed consent

---

## The Research Vision

### Core Question
**How do humans actually collaborate with Large Language Models in practice?**

We don't have good empirical data on this yet. Most discussions about "AI overreliance" or "effective prompting" are based on:
- Individual anecdotes
- Small lab studies
- Assumptions about what people *should* do

**Turn flips this:** Let's observe what people *actually* do, in their real work, over time.

### What Makes This Dataset Unique

Unlike traditional research datasets:
- ✅ **Longitudinal** - Track patterns over weeks/months, not single sessions
- ✅ **Naturalistic** - Real work, not lab tasks
- ✅ **Self-reported** - People define what actions matter to them
- ✅ **Reflexive** - The act of tracking may change behavior (and that's interesting!)
- ✅ **Community-generated** - Actions and patterns emerge from users, not researchers
- ✅ **Open access** - No paywalls, anyone can analyze it

---

## Data Collection

### What Gets Tracked (Automatically)

When you use Turn, the following is recorded locally:

**Session-level:**
- Session start/end timestamps
- Session name (if you provide one)
- Final scores (user points, LLM points)
- Status (active, paused, ended)

**Action-level:**
- Timestamp of when action was tracked
- Action description (e.g., "Asked LLM to explain code")
- Points allocated (user movement, LLM movement)
- Source (library action, custom action, or session-specific)

**Library-level:**
- Custom actions you create
- How many times each action is used
- Whether it originated from starter set or user-created

### What Is NOT Tracked

- ❌ Email addresses (anonymized before export)
- ❌ Actual code or text you're working on
- ❌ Which specific LLM you're using (ChatGPT, Claude, etc.)
- ❌ Your prompts or LLM responses
- ❌ Any content outside the Turn interface
- ❌ Location, IP address, device info

---

## Privacy & Anonymization

### How Your Data Is Protected

**1. Local-First Architecture**
- All data lives on YOUR machine by default
- Nothing is sent to any server unless you explicitly export
- You can use Turn forever without sharing anything

**2. Anonymization Process**
When you choose to "Export for Research," here's what happens:

```javascript
// Original data (stays on your machine)
{
  email: "amy@university.edu",
  session_name: "Working on dissertation chapter 3",
  actions: [
    { description: "Asked Claude to summarize this paper", timestamp: "2025-01-15 14:32:10" }
  ]
}

// Anonymized export (what gets shared)
{
  user_id: "sha256_hash_abc123",  // One-way hash, can't reverse to email
  session_name: null,  // Removed
  session_duration_minutes: 47,
  actions: [
    {
      description: "Asked Claude to summarize this paper",  // Generic description kept
      timestamp_relative: 180,  // Seconds since session start (not absolute time)
      user_points: 2,
      llm_points: 3
    }
  ]
}
```

**3. What the Hash Means**
- Your email is converted to a random-looking ID like `user_a3f7b9c2`
- This allows linking your different sessions without knowing who you are
- Same email = same hash (so we can see patterns over time)
- Different email = different hash (so we can count unique users)
- **Impossible to reverse** - we can't figure out your email from the hash

---

## Optional Demographics Survey

When you export for research, you'll be invited (but not required) to answer:

### Basic Demographics
- Age range: `<20`, `20-29`, `30-39`, `40-49`, `50+`, `Prefer not to say`
- Gender: Open text or `Prefer not to say`
- Country: Dropdown list
- Primary language: Dropdown list

### Professional Context
- Role: `Student`, `Software Engineer`, `Researcher`, `Writer`, `Designer`, `Data Analyst`, `Teacher`, `Other`, `Prefer not to say`
- Years of professional experience: `0-2`, `3-5`, `6-10`, `10+`, `Prefer not to say`
- Industry: `Tech`, `Academia`, `Healthcare`, `Creative`, `Finance`, `Other`, `Prefer not to say`

### LLM Experience
- How long have you been using LLMs? `<6 months`, `6-12 months`, `1-2 years`, `2+ years`, `Prefer not to say`
- How often do you use LLMs? `Daily`, `Weekly`, `Monthly`, `This is my first time`, `Prefer not to say`
- Primary LLM tool: `ChatGPT`, `Claude`, `GitHub Copilot`, `Gemini`, `Other`, `Multiple`, `Prefer not to say`

### Reflection Questions (Optional Text)
- Why did you start tracking your LLM collaboration patterns?
- What has surprised you most about your patterns?
- Has tracking changed how you work with LLMs?

**These answers are saved separately** as `user_abc123_demographics.json` and can be skipped entirely.

---

## The Public Dataset

### Where It Lives

**GitHub Repository:** `turn-research-data` (separate from main app repo)

```
turn-research-data/
├── README.md                    # How to use this dataset
├── ETHICS.md                    # Ethics approval, consent process
├── data/
│   ├── sessions/
│   │   ├── batch_2025_01/
│   │   │   ├── user_001.csv
│   │   │   ├── user_002.csv
│   │   │   └── ...
│   ├── demographics/
│   │   ├── batch_2025_01/
│   │   │   ├── user_001.json
│   │   │   └── ...
│   └── aggregated/
│       ├── all_sessions_2025_Q1.csv
│       └── all_demographics_2025_Q1.csv
├── analysis/
│   ├── notebooks/
│   │   ├── 01_exploratory_analysis.ipynb
│   │   ├── 02_action_patterns.ipynb
│   │   └── 03_demographic_differences.ipynb
│   └── visualizations/
│       ├── common_actions_wordcloud.png
│       └── score_distributions.png
└── publications/
    ├── papers.md               # List of papers using this data
    └── citations.bib           # How to cite the dataset
```

### Data Formats

**Session CSV format:**
```csv
user_id,session_duration_min,user_score,llm_score,action_count,timestamp_relative_sec,action_description,user_points,llm_points,action_source
user_a3f,45,12,8,5,0,Started new coding task,0,0,library
user_a3f,45,12,8,5,120,Asked LLM to write function,0,3,library
user_a3f,45,12,8,5,240,Reviewed LLM code for bugs,3,0,library
user_a3f,45,12,8,5,600,Modified LLM code significantly,4,-1,library
user_a3f,45,12,8,5,1800,Asked LLM to explain approach,1,2,custom
```

**Demographics JSON format:**
```json
{
  "user_id": "user_a3f7b9c2",
  "age_range": "30-39",
  "gender": "prefer_not_to_say",
  "country": "USA",
  "role": "Software Engineer",
  "years_experience": "6-10",
  "years_using_llms": "1-2",
  "primary_llm": "Claude",
  "submitted_at": "2025-01-15"
}
```

---

## How to Contribute Your Data

### Step 1: Use Turn
Track your LLM collaboration for at least a few sessions (the more the better!).

### Step 2: Export for Research
Click the **"Export for Research"** button in the Dashboard or session view.

### Step 3: Review What's Being Shared
You'll see a preview of your anonymized data. Check that you're comfortable sharing it.

### Step 4: Optional Demographics Survey
Fill out as much or as little as you want. Every question has "Prefer not to say."

### Step 5: Submit to GitHub
Two options:

**Option A: GitHub PR (if you're comfortable with Git)**
1. Fork the `turn-research-data` repository
2. Add your `user_xxx.csv` file to `data/sessions/batch_YYYY_MM/`
3. Add your `user_xxx.json` file to `data/demographics/batch_YYYY_MM/` (if you filled it out)
4. Submit a Pull Request

**Option B: Email/Form (easier)**
1. Email your exported files to [research email]
2. Or upload via Google Form [link when ready]
3. We'll add them to the repo and credit you in the contributors list

### You Can Withdraw Anytime
Email us with your user_id hash and we'll remove your data from future releases.

---

## Using This Dataset

### For Researchers

**Citation:**
```
@dataset{turn_collaboration_dataset_2025,
  title={Turn: Human-LLM Collaboration Patterns Dataset},
  author={Turn Community Contributors},
  year={2025},
  publisher={GitHub},
  url={https://github.com/username/turn-research-data}
}
```

**Potential Research Questions:**
- How do collaboration patterns differ by profession, experience, or demographics?
- What actions do people track most frequently?
- Do users become more passive (higher LLM scores) over time?
- How do custom actions differ from starter library actions?
- What linguistic patterns appear in action descriptions?
- Can we identify "collaboration styles" through cluster analysis?
- Does self-tracking change behavior (compare early vs. late sessions)?

### For Teachers & Students

**Classroom Activities:**

**Week 1: Start Tracking**
- Students install Turn
- Track their LLM usage for 2-4 weeks during coursework
- Weekly reflection: "What surprised you about your patterns?"

**Week 4: Analyze Your Own Data**
- Export personal CSV
- Load into Python/R/Excel
- Create visualizations of their patterns
- Write reflection paper on their collaboration style

**Week 6: Compare with Class Dataset**
- Aggregate (anonymized) class data
- Students analyze: "How do I compare to my peers?"
- Discussion: "Why do we see these differences?"

**Week 8: Analyze Public Dataset**
- Download full Spade research dataset
- Students propose and answer research questions
- Practice: data cleaning, visualization, statistical testing
- Final project: Present findings to class

**Benefits:**
- Students learn data analysis on data they deeply understand (their own!)
- Immediate relevance (we're all using LLMs now)
- Ethics discussion built-in (privacy, anonymization, consent)
- Develops metacognition about AI use
- Contributes to real research

### For Data Scientists & Hobbyists

**Kaggle-Style Challenges:**
- Can you predict a user's profession from their action patterns?
- Build a "collaboration style" classifier
- Identify common sequences of actions
- Create beautiful visualizations of patterns
- NLP analysis of custom action descriptions

**Notebook Gallery:**
Share your analysis notebooks! We'll feature the best ones in the repo.

---

## Ethics & Informed Consent

### Consent Process

When you click "Export for Research," you'll see:

```
┌─────────────────────────────────────────────────────────┐
│  Contribute to Human-LLM Collaboration Research         │
│                                                         │
│  By sharing your data, you consent to:                 │
│  ✓ Anonymized session data being publicly released     │
│  ✓ Anyone (researchers, students, hobbyists) using it  │
│  ✓ Findings being published in papers/blogs/articles   │
│  ✓ Your individual sessions potentially being quoted   │
│    as examples (but never linked to you)               │
│                                                         │
│  Your privacy is protected by:                         │
│  ✓ Email addresses replaced with one-way hashes        │
│  ✓ Absolute timestamps converted to relative times     │
│  ✓ Session names and personal notes removed            │
│  ✓ No content from your actual work included           │
│                                                         │
│  You retain the right to:                              │
│  ✓ Withdraw your data anytime (we'll remove it)        │
│  ✓ Request information about how it's being used       │
│  ✓ See the full public dataset before contributing     │
│                                                         │
│  [ View Anonymized Preview ]                           │
│                                                         │
│  [ ] I understand and consent to share this data       │
│                                                         │
│  [ Cancel ]  [ Export for Research ]                   │
└─────────────────────────────────────────────────────────┘
```

### IRB / Ethics Approval

**Status:** This project is open source and community-driven. If you're a researcher who wants to publish papers using this dataset, you should:

1. **Check with your institution's IRB** - Some may consider this "existing public data" (exempt), others may want documentation
2. **Cite the consent process** - Point to this RESEARCH.md document
3. **Follow your field's norms** - HCI, Education, Sociology all have different standards

**For course instructors:** If you want students to contribute class data, check with your IRB first. Most will consider it "educational activity" but it's worth confirming.

### Potential Risks

We've tried to minimize risks, but users should know:

**Low Risk:**
- Someone might infer your profession from action patterns (but not your identity)
- Action descriptions might include work-related info (e.g., "debugging React app" reveals you work with React)

**Mitigation:**
- Review your export before submitting
- Edit any action descriptions that feel too specific
- Don't submit if you're uncomfortable

### Data Retention & Deletion

- Data is stored indefinitely in the public GitHub repo (that's the point!)
- If you want your data removed, email us with your `user_id` hash
- We'll remove it from the **next** release, but past releases/publications can't be recalled
- Consider this before submitting - think of it like posting to a public forum

---

## Frequently Asked Questions

**Q: Can someone de-anonymize me from the hash?**
A: Extremely unlikely. It's a one-way cryptographic hash (SHA-256). The only way would be if someone had a database of emails and tried hashing each one until they found a match - but that requires knowing you're in the dataset and having your email.

**Q: What if I accidentally include sensitive info in an action description?**
A: Review your export before submitting! You can edit the CSV to remove/redact anything. Or just don't submit that session.

**Q: Can I see the dataset before deciding to contribute?**
A: Yes! It's public on GitHub. Browse it first: [link to repo when ready]

**Q: What if my employer doesn't want me sharing work patterns?**
A: Don't share! Or ask first. The data is generic enough that it probably doesn't reveal trade secrets, but check your employment agreement.

**Q: Can I submit data on behalf of a research study?**
A: Yes, but get proper IRB approval first. Make sure participants consent to public data sharing, not just your research.

**Q: Do I get credit if I contribute data?**
A: Contributors are listed in the repo README (by user_id hash, not real name). If you want your real name credited, include it in the demographic survey's optional text field.

**Q: Can I contribute data from my students (I'm a teacher)?**
A: Only if they're adults (18+) and give informed consent. Minors' data requires parental consent and stricter IRB review - probably not worth it.

**Q: Will you make money from this dataset?**
A: No. It's MIT licensed - we can't stop others from using it commercially, but we won't. If someone builds a startup using insights from this data, good for them! The dataset remains free forever.

---

## Roadmap

### Phase 1: Manual Submission (Current)
- ✅ Define anonymization process
- ✅ Create data format standards
- 🚧 Set up `turn-research-data` GitHub repo
- 🚧 Create submission form/email process
- 🚧 Write ethics documentation

### Phase 2: Automated Export (Next)
- Build "Export for Research" button into app
- Show consent dialog with preview
- Generate anonymized CSV automatically
- Optional demographics survey popup
- Easy one-click submission

### Phase 3: Initial Dataset Release
- Collect at least 50-100 contributors
- Release v1.0 of dataset
- Publish blog post announcing it
- Reach out to research communities
- Create starter analysis notebooks

### Phase 4: Community Growth
- Host Kaggle competition or challenge
- Featured "Insight of the Month" from community analysis
- Partner with courses/bootcamps to use as teaching dataset
- Publish first academic paper using the data

---

## Get Involved

**I want to contribute data:**
- Use the app, then click "Export for Research" (coming soon!)
- Or email exported CSV to [email]

**I want to analyze the data:**
- Clone the `turn-research-data` repo
- Try the Jupyter notebooks in `/analysis`
- Share your findings! (PRs welcome)

**I'm teaching a course and want to use this:**
- Email us! We'll help you design classroom activities
- Share your syllabus/activities (we'll feature them)

**I'm a researcher and want to collaborate:**
- Open an issue on GitHub to propose research questions
- Co-author papers using the dataset
- Help with ethics review and methodology

---

## Contact

- **GitHub Issues:** [github.com/username/turn-app/issues](https://github.com/username/turn-app/issues)
- **Research Inquiries:** [your research email]
- **Collaborations:** [your email]

---

**Remember:** Every action you track is a tiny ethnographic observation. Together, we're building a collective understanding of how humans navigate this weird, wonderful new era of working alongside AI. Thank you for being part of it! 🔬🔄

---

*This research methodology was co-designed by humans and LLMs. Meta-commentary on human-LLM collaboration while designing tools to study human-LLM collaboration is encouraged.* 😄
