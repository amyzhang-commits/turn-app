# 🔄 Turn: Vision & Research Goals

## What is Turn?

Turn is a **gamified reflection tool** that helps people become more aware of their collaboration patterns with Large Language Models (LLMs). It transforms the abstract question of "Am I working *with* the AI or just letting it work *for* me?" into a concrete, trackable game.

## The Core Metaphor: Turn

The technical term for every interaction in the conversation with an LLM is a 'turn'. We join this with the context of turn-based games to create an app that asks, **Whose turn is it**--to make a move, to flex their agency?

When you work with an LLM, every interaction moves the "growth balance" somewhere:
- **You advance** when you actively shape, critique, or guide the AI
- **LLM advances** when you passively accept outputs without engagement
- **Balanced moves** approach genuine teamwork

The goal isn't to "beat" the LLM -- and even less so to beat yourself up. Turn is a device meant to help you **notice your patterns**, be objective in your (self) assessments, and decide what changes might better serve your goals.

## Why This Matters

LLMs are staggeringly capable—producing outputs at many times the speed of a single individual, and sometimes, especially when you're venturing outside a familiar domain, of much higher caliber.

While many of us embrace the possibilities of this new creative relationship, the question of balance looms large. How much should we lean on the tireless machine versus our own efforts? Debates rage on, while justifiably concerned parents and educators hastily assemble lists of Do's and Don'ts.

The goal of Turn is to…well…*turn* the general sense of unease into something we can objectively assess. You feel like you're probably getting overly reliant—but in what ways, and is it as often as you imagine? If there's a problem, we can only tackle it when we're clear on the current situation.

And speaking of the current situation: Turn invites us to notice that while learning will always require friction—the kind LLMs can seem to make optional—industrial-era constructs like "productivity" and "efficiency" are in a real moment of flux.

We're accomplishing tasks we couldn't have undertaken before, or doing classical tasks in entirely new ways. Before judging outright, how about just *tracking* what patterns emerge as we navigate this landscape of working hard and working smart?

## EXPANDED: The Research Vision

Beyond a kind of personal productivity tool, Turn hopes to be a **public ethnographic database** of human-LLM collaboration.

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

- **GitHub:** [github.com/amyzhang-commits/turn-app](https://github.com/amyzhang-commits/turn-app)
- **Issues:** Use GitHub issues for bugs/features
- **Discussions:** Use GitHub Discussions for questions/ideas
- **Research inquiries:** amy.pairtree@gmail.com

---

**This document was created in collaboration with Claude (Anthropic) - a fitting origin for a tool about human-AI collaboration. Embracing the moment!** 😄
