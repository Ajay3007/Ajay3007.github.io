---
layout: default
title: Home
---

# 👋 Welcome to ajdevhub

My personal hub for projects, blogs, and learning resources in programming..


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


## 📝 Latest Blog Posts

{% for post in site.posts limit: 3 %}
- **[{{ post.title }}]({{ post.url }})** - <time>{{ post.date | date: "%B %d, %Y" }}</time>
{% endfor %}

[Read More Posts →]({{ '/blogs' | relative_url }})


## 📚 Learning Journey

Explore topic-wise paths and quick intros below.

<div class="projects-list">
    <div class="project-card">
        <h3><a href="{{ '/learning/data-structures/' | relative_url }}">Data Structures & Algorithms</a></h3>
        <p>Fundamentals, implementations, and problem-solving patterns.</p>
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



## 💡 About This Site

This portfolio showcases my journey in programming, learning data structures & Algorithm. Feel free to explore my work and [learn more about me]({{ '/about' | relative_url }}).

