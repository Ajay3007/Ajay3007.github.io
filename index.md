---
layout: default
title: Home
permalink: /
---

# 👋 Welcome to ajdevhub

My personal hub for projects, blogs, and learning resources in programming..

## 📝 Latest Blog Posts

{% for post in site.posts limit: 3 %}
- **[{{ post.title }}]({{ post.url }})** - <time>{{ post.date | date: "%B %d, %Y" }}</time>
{% endfor %}

[Read More Posts →]({{ '/blogs' | relative_url }})


## 📚 Learning Journey

Explore topic-wise paths and quick intros below.

<div class="projects-list">
    <!-- <div class="project-card">
        <h3><a href="{{ '/learning/data-structures/' | relative_url }}">Data Structures & Algorithms</a></h3>
        <p>Fundamentals, implementations, and problem-solving patterns.</p>
    </div> -->
    <div class="project-card">
        <h3>
          <svg class="card-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M3 6.5C3 5.12 4.12 4 5.5 4h13C20.88 4 22 5.12 22 6.5v11c0 1.38-1.12 2.5-2.5 2.5h-13C4.12 20 3 18.88 3 17.5v-11zM6 7v10h12V7H6z"/></svg>
          <a href="{{ '/learning/data-structures/' | relative_url }}">Data Structures & Algorithms</a>
        </h3>
        <p>Fundamentals, implementations, and problem-solving patterns.</p>
        <ul class="sub-links">
          <li><a href="{{ '/learning/data-structures/arrays/' | relative_url }}">Arrays</a> · <a href="{{ '/learning/data-structures/arrays/two-pointers/' | relative_url }}">Two Pointers</a> · <a href="{{ '/learning/data-structures/arrays/sliding-window/' | relative_url }}">Sliding Window</a></li>
          <li><a href="{{ '/learning/data-structures/linked-list/' | relative_url }}">Linked List</a> · <a href="{{ '/learning/data-structures/trees/' | relative_url }}">Trees</a></li>
          <li><a href="{{ '/learning/data-structures/sorting/' | relative_url }}">Sorting</a> · <a href="{{ '/learning/data-structures/dynamic-programming/' | relative_url }}">Dynamic Programming</a> · <a href="{{ '/learning/data-structures/graphs/' | relative_url }}">Graphs</a></li>
        </ul>
      </div>
    <div class="project-card">
        <h3><a href="{{ '/learning/system-design/' | relative_url }}">System Design</a></h3>
        <p>High-level architecture, scalability, and trade-offs.</p>
    </div>
    <div class="project-card">
        <h3><a href="{{ '/learning/oop/' | relative_url }}">OOPs</a></h3>
        <p>Core principles, SOLID, and design patterns.</p>
    </div>
    <div class="project-card">
        <h3><a href="{{ '/learning/operating-systems/' | relative_url }}">Operating Systems</a></h3>
        <p>Processes, memory, scheduling, and concurrency.</p>
    </div>
    <div class="project-card">
        <h3><a href="{{ '/learning/networking/' | relative_url }}">Networking</a></h3>
        <p>Protocols, routing, TCP/UDP and practical networking.</p>
    </div>
    <div class="project-card">
        <h3><a href="{{ '/learning/competitive-programming/' | relative_url }}">Competitive Programming</a></h3>
        <p>Contest strategy, patterns and practice resources.</p>
    </div>
    <div class="project-card">
                <h3><a href="{{ '/learning/ai-ml/' | relative_url }}">AI & ML</a></h3>
                <p>Introductory ML concepts, models and projects.</p>
    </div>
</div>

[Explore full learning index →]({{ '/learning' | relative_url }})

## 🚀 Latest Projects

<div class="projects-list">
    {% for project in site.projects limit: 3 %}
    <div class="project-card">
        <h3><a href="{{ project.url }}">{{ project.title }}</a></h3>
        {% if project.description %}
            <p>{{ project.description }}</p>
        {% endif %}
    </div>
    {% endfor %}
</div>


[View All Projects →]({{ '/projects' | relative_url }})


## 💡 About This Site

This portfolio showcases my journey in programming, learning data structures & Algorithm. Feel free to explore my work and [learn more about me]({{ '/about' | relative_url }}).

