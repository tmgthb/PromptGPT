# PromptGPT

## Introduction

PromptGPT is a systematic approach for creating [autonomous agents](https://en.wikipedia.org/wiki/Autonomous_agent) with [Large Language Models (LLMs)](https://en.wikipedia.org/wiki/Large_language_model) with models such as [GPT-4](https://arxiv.org/abs/2303.08774), ChatGPT 3.5-turbo, Antropic or similar fine-tuned LLM with [Reinforcement Learning with Human Feedback (RLHF)](https://arxiv.org/abs/2203.02155). 

## Core principles

The core principles of PromptGPT are simple:
- Autonomous, self-supportive & objective-agnostic workflows.
- Versatile, generic functions submit API calls to GPT models.
- Define scope, objective and checkpoints (exit criteria) only once.
- Centralize pre-defined settings under Control panel: user/system-instructions, models, context lengths and resources.
- Option to learn additional capabilities autonomously.
- User-interface agnostic: Jupyter Notebooks, Streamlit-chatbots, Flask-apps, etc. Support embedded experiences.

## Functions
- All functions are versatile and generic.
- For example an API call to LLM uses only single, generic function. 
- Functions enable repeating steps, such as saving data to memory, using resources and retrieving task description and role.

## Control panel
- Simple with zero configuration required.
- Option to add new functions automatically or modify them manually.

## Plans
- PromptGPT automatically generates workflow plan and components.
- Workflow components are managed autonomously.
- Workflow components include task: definition, role, resources and status.

## Resources
- Resources include workflows and data performed stored outside the Prompt-GPT flow.
- Resource types include internal memory, API calls.
- New resource types are supported. 

## Checkpoints
- An optional, structured method for steerability, safety and exit criteria.
- Define exit criteria: limit token consumption, forbid specific behaviour and increase steerability. 
- For example, specific types of roles / tasks trigger the flow to automatically exit.

## User-Interface vs. Embedded Experiences
- The first release uses Jupyter Notebook as the user-interface and the idea is to extend the code to wide variety of user interfaces: voice, chat etc. 
- PromptGPT works behind the scenes, where another action may trigger the flow to begin, progress and/or complete.


## Contributing
PromptGPT is an open source project, where anybody can contribute for external appreciation. Build on top by forking the current version of the repository, make changes to your forked version and then open a pull request to the main repository with the updated version. [How to contribute](https://docs.github.com/en/get-started/quickstart/contributing-to-projects)

## Licensing
Released under MIT license.
