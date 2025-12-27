---
layout: default
title: Projects
permalink: /projects/
---

# Projects

A catalog of my work. Items from the `projects` collection:

<ul class="projects-list">
{% for p in site.projects %}
  <li class="project-card">
    <h3>{{ p.title }}</h3>
    <div class="project-content">{{ p.content }}</div>
  </li>
{% endfor %}
</ul>
