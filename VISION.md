# 🎮 Turn: Vision & Research Goals

## What is Turn?

Turn is a **gamified reflection tool** that helps people become more aware of their collaboration patterns with Large Language Models (LLMs). It transforms the abstract question of "Am I working *with* the AI or just letting it work *for* me?" into a concrete, trackable game.

## The Core Metaphor: Turn

In card games, taking turns represents effort, work, and intentionality. This app asks: **Whose turn is it?**

When you work with an LLM, every interaction moves the "control balance" somewhere:
- **You advance** when you actively shape, critique, or guide the AI
- **LLM advances** when you passively accept outputs without engagement
- **Balanced moves** represent genuine collaboration

The goal isn't to "beat" the LLM or keep it from advancing - it's to **notice your patterns** and decide if they serve your goals.

## Why This Matters

As LLMs become more capable, there's a risk of "learned helplessness" where humans:
- Stop understanding their own code
- Lose the ability to debug without AI assistance
- Become less creative problem solvers
- Miss opportunities for deep learning

But there's also a risk of **rejecting useful collaboration** out of pride or fear.

**Turn says:** There's no "right" way to work with LLMs. But **awareness** is essential. Track your patterns, reflect on them, and make intentional choices about your human-AI workflow.

## The Research Vision

This isn't just a personal productivity tool - it's a **public ethnographic database** of human-LLM collaboration.

### Research Questions We Can Explore:

1. **Patterns Across Domains**
   - How do programmers track collaboration differently than writers?
   - What actions do data scientists value vs. designers?

2. **Temporal Dynamics**
   - Do people become more passive with LLMs over time?
   - How does collaboration change within a single work session?

3. **Custom Action Ecology**
   - What kinds of actions do people invent beyond our starter set?
   - How do communities develop shared vocabularies for AI collaboration?

4. **Cultural Differences**
   - Do collaboration patterns differ across languages, countries, work cultures?
   - How does organizational context shape human-AI dynamics?

5. **Reflection & Metacognition**
   - Does tracking these patterns change behavior?
   - What insights do people gain from reviewing their session data?

### Making This Public Research Possible

We want to build a **privacy-preserving, opt-in research database** where:

✅ **Users maintain control** - You run the app locally, your data stays on your machine
✅ **Sharing is optional** - Export anonymized data when YOU want to contribute
✅ **Full transparency** - All analysis code is public, you can see what we're studying
✅ **Community-driven** - Researchers, practitioners, and curious humans collaborate on insights

## Architecture Philosophy

### Core Principles:

1. **Privacy First**
   - Default mode: Everything stored locally
   - No tracking, no analytics, no data leaves your machine without consent
   - Email only used for authentication, never shared

2. **Self-Hostable**
   - Open source from day one
   - Easy to run on your own machine (or deploy your own instance)
   - No vendor lock-in, you can export all your data anytime

3. **Transparent**
   - All code is readable and modifiable
   - Database schema is documented
   - Export formats are simple CSV/JSON - no proprietary formats

4. **Community-Extensible**
   - Want to track different actions? Fork it!
   - Want different point systems? Customize it!
   - Want to visualize data differently? Build on it!

## Deployment Options

### Option 1: Local-Only (Most Private)
```
You → Download from GitHub
    → Run on your machine (localhost)
    → Your data never leaves your computer
    → Export CSV if you want to share for research
```

**Best for:** Privacy-conscious users, corporate environments, personal use

### Option 2: Public Demo Instance (Easiest)
```
You → Visit hosted instance (e.g., turn.app)
    → Sign up with email
    → Data stored in shared database
    → Can export/delete anytime
    → Opt-in to contribute anonymized data for research
```

**Best for:** Trying it out, non-technical users, sharing with friends

### Option 3: Self-Host Your Instance (Middle Ground)
```
You → Deploy to your own Railway/Heroku/VPS
    → Control your own database
    → Invite your team/community
    → Decide your own data policies
```

**Best for:** Research groups, companies, communities who want control

## Roadmap

### Phase 1: Core Experience ✅ (We are here!)
- [x] Session tracking with point system
- [x] Action library with starter actions
- [x] Custom action creation
- [x] Real-time score visualization
- [x] CSV export for analysis
- [x] Multi-user authentication
- [x] Action timestamps

### Phase 2: Easy Deployment 🚧 (Next up)
- [ ] Docker Compose setup for one-command install
- [ ] Comprehensive README with installation guide
- [ ] Video tutorial for non-technical users
- [ ] One-click deploy buttons (Railway, Replit)
- [ ] Desktop app builds (Electron - optional)

### Phase 3: Research Infrastructure 🔮 (Future)
- [ ] Anonymized export format standardized
- [ ] Public research data repository (spade-research-data)
- [ ] Analysis notebooks (Jupyter) for pattern exploration
- [ ] Public dashboard showing aggregate insights
- [ ] Ethics review & informed consent flow
- [ ] API for researchers to query anonymized data

### Phase 4: Community Features 🔮 (Future)
- [ ] Share custom action libraries
- [ ] Compare your patterns with community averages
- [ ] Reflection prompts based on your patterns
- [ ] Integration with time-tracking tools
- [ ] Browser extension for passive tracking (opt-in)
- [ ] Visualizations: heatmaps, trend lines, pattern recognition

## How to Contribute

### As a User:
1. **Use it & give feedback** - Does it help you reflect? What's missing?
2. **Share your custom actions** - What did you track that we didn't think of?
3. **Export & share data** - Contribute anonymized sessions for research (when ready)
4. **Tell your story** - Blog/tweet about your insights from using Spade

### As a Developer:
1. **Report bugs** - GitHub issues are welcome!
2. **Suggest features** - What would make this more useful?
3. **Submit PRs** - Improvements to code, docs, or design
4. **Fork & customize** - Make it work for your specific use case
5. **Help with deployment** - Make self-hosting easier

### As a Researcher:
1. **Propose research questions** - What should we study?
2. **Contribute analysis code** - Jupyter notebooks, visualizations
3. **Ethics review** - Help us do this responsibly
4. **Publication collaboration** - Co-author papers on findings

## Success Metrics

**For Individuals:**
- "I understand my collaboration patterns better"
- "I made an intentional change in how I work with AI"
- "I feel more in control of my learning"

**For the Community:**
- Active discussions about human-AI collaboration patterns
- Diverse custom actions being created and shared
- Meaningful research insights published from the data
- Other tools/papers building on this work

**For the Field:**
- New vocabulary for describing human-AI collaboration
- Evidence-based guidelines for effective AI partnership
- Recognition that collaboration patterns are diverse and contextual
- Less guilt, more intentionality in how we work with AI

## License & Ethics

- **Code:** MIT License (open source, do whatever you want)
- **Data:** All user data remains yours, anonymized sharing is opt-in only
- **Research:** Any publications will follow standard ethics protocols
- **Commercial Use:** Totally allowed! If you make money with this, great!

## Contact & Community

- **GitHub:** [github.com/yourusername/turn-app](https://github.com/yourusername/turn-app)
- **Issues:** Use GitHub issues for bugs/features
- **Discussions:** Use GitHub Discussions for questions/ideas
- **Research inquiries:** [your email or contact form]

---

## A Note on the Name

**Turn** captures multiple meanings:
- 🔄 Taking turns - the back-and-forth of human-AI collaboration
- 🎮 "Your turn" - active engagement, agency, intentionality
- 📖 "Turn the page" - moving forward, reflection, new chapters
- 🔍 "Turn your attention to..." - mindful awareness of patterns

The name emphasizes that collaboration is a dynamic exchange, not a zero-sum game. Sometimes it's your turn to lead, sometimes the AI's - and that's okay.

---

## Final Thoughts

This project emerges from a belief that **tools shape thinking**.

By making collaboration patterns *visible* and *trackable*, we create space for reflection. By making this reflection *public* (when people choose), we enable collective learning about this profound shift in how humans create.

We don't know yet what the "right" patterns are. Maybe there aren't universal answers. But we can learn together, and we can help each other stay intentional, curious, and human as AI becomes more capable.

Your turn. 🔄

---

**This document was created in collaboration with Claude (Anthropic) - a fitting origin for a tool about human-AI collaboration. The irony is not lost on us.** 😄
