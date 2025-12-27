---
layout: default
title: Projects
permalink: /projects/
---

# 🛠️ Projects

Here are some of my latest projects and explorations:

<div class="projects-list">
{% for project in site.projects %}
    <div class="project-card">
        <h3><a href="{{ project.url }}">{{ project.title }}</a></h3>
        {% if project.description %}
            <p>{{ project.description }}</p>
        {% endif %}
    </div>
{% endfor %}
</div>
