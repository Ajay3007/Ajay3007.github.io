---
layout: default
title: Home
---

# 👋 Welcome to ajdevhub

My personal hub for projects, blogs, and learning resources in programming and Computer Science & Engineering.


<div class="home-top">
    <div class="hf-tabs">
        <div class="hf-tab active" data-target="overview">Overview</div>
        <div class="hf-tab" data-target="activity">Activity</div>
    </div>
    <div class="home-search">
        <input id="home-search" type="search" placeholder="Search projects & posts..." aria-label="Search" />
        <a href="{{ '/projects' | relative_url }}" role="button">All Projects</a>
    </div>
    <div id="overview" class="hf-panel active">
        <div style="display: grid; gap: 2rem;">
            <!-- Intro Section -->
            <div style="background: linear-gradient(135deg, rgba(0,212,255,0.08), rgba(255,107,157,0.08)); border-radius: 12px; padding: 2rem; border: 1px solid rgba(0,212,255,0.1);">
                <h2 style="margin: 0 0 0.75rem 0; color: var(--primary-color);">👨‍💻 Welcome</h2>
                <p style="margin: 0; color: var(--light-text); line-height: 1.8; font-size: 1.05rem;">
                    Software Engineer with 4+ years building high-performance systems in <strong>networking</strong>, <strong>data plane</strong>, and <strong>backend infrastructure</strong>. 
                    Passionate about system design, deep packet inspection, and real-time threat detection.
                </p>
            </div>

            <!-- Stats Section -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1.5rem;">
                <div style="background: white; padding: 1.5rem; border-radius: 10px; text-align: center; box-shadow: var(--shadow-sm); border-top: 3px solid var(--secondary-color);">
                    <div style="font-size: 2.2rem; font-weight: 700; color: var(--secondary-color);">{{ site.posts | size }}</div>
                    <div style="color: var(--light-text); font-size: 0.95rem; font-weight: 600;">Blog Posts</div>
                </div>
                <div style="background: white; padding: 1.5rem; border-radius: 10px; text-align: center; box-shadow: var(--shadow-sm); border-top: 3px solid var(--accent-color);">
                    <div style="font-size: 2.2rem; font-weight: 700; color: var(--accent-color);">{{ site.projects | size }}</div>
                    <div style="color: var(--light-text); font-size: 0.95rem; font-weight: 600;">Projects</div>
                </div>
                <div style="background: white; padding: 1.5rem; border-radius: 10px; text-align: center; box-shadow: var(--shadow-sm); border-top: 3px solid #9945ff;">
                    <div style="font-size: 2.2rem; font-weight: 700; color: #9945ff;">10+</div>
                    <div style="color: var(--light-text); font-size: 0.95rem; font-weight: 600;">Topics</div>
                </div>
            </div>

            <!-- Key Areas -->
            <div>
                <h3 style="color: var(--primary-color); margin-top: 0; margin-bottom: 1.25rem;">🎯 Explore by Interest</h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem;">
                    <a href="{{ '/learning/dsa/' | relative_url }}" style="padding: 1.25rem; background: white; border-radius: 8px; text-decoration: none; color: var(--primary-color); border-left: 4px solid #00d4ff; transition: all 0.2s; box-shadow: var(--shadow-sm);" onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='var(--shadow)';" onmouseout="this.style.transform='none'; this.style.boxShadow='var(--shadow-sm)';">
                        <div style="font-weight: 700; margin-bottom: 0.3rem;">📊 DSA & Algorithms</div>
                        <div style="font-size: 0.9rem; color: var(--light-text);">Structures, patterns & solutions</div>
                    </a>
                    <a href="{{ '/learning/system-design/' | relative_url }}" style="padding: 1.25rem; background: white; border-radius: 8px; text-decoration: none; color: var(--primary-color); border-left: 4px solid #ff6b9d; transition: all 0.2s; box-shadow: var(--shadow-sm);" onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='var(--shadow)';" onmouseout="this.style.transform='none'; this.style.boxShadow='var(--shadow-sm)';">
                        <div style="font-weight: 700; margin-bottom: 0.3rem;">🏗️ System Design</div>
                        <div style="font-size: 0.9rem; color: var(--light-text);">Architecture & scalability</div>
                    </a>
                    <a href="{{ '/learning/networking/' | relative_url }}" style="padding: 1.25rem; background: white; border-radius: 8px; text-decoration: none; color: var(--primary-color); border-left: 4px solid #9945ff; transition: all 0.2s; box-shadow: var(--shadow-sm);" onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='var(--shadow)';" onmouseout="this.style.transform='none'; this.style.boxShadow='var(--shadow-sm)';">
                        <div style="font-weight: 700; margin-bottom: 0.3rem;">🌐 Networking</div>
                        <div style="font-size: 0.9rem; color: var(--light-text);">Protocols & data plane</div>
                    </a>
                    <a href="{{ '/learning/data-plane/' | relative_url }}" style="padding: 1.25rem; background: white; border-radius: 8px; text-decoration: none; color: var(--primary-color); border-left: 4px solid #00d4ff; transition: all 0.2s; box-shadow: var(--shadow-sm);" onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='var(--shadow)';" onmouseout="this.style.transform='none'; this.style.boxShadow='var(--shadow-sm)';">
                        <div style="font-weight: 700; margin-bottom: 0.3rem;">⚡ Data Plane (DPDK/VPP)</div>
                        <div style="font-size: 0.9rem; color: var(--light-text);">Performance & optimization</div>
                    </a>
                    <a href="{{ '/learning/oop/' | relative_url }}" style="padding: 1.25rem; background: white; border-radius: 8px; text-decoration: none; color: var(--primary-color); border-left: 4px solid #ff6b9d; transition: all 0.2s; box-shadow: var(--shadow-sm);" onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='var(--shadow)';" onmouseout="this.style.transform='none'; this.style.boxShadow='var(--shadow-sm)';">
                        <div style="font-weight: 700; margin-bottom: 0.3rem;">🎯 OOP & Patterns</div>
                        <div style="font-size: 0.9rem; color: var(--light-text);">Design principles & patterns</div>
                    </a>
                    <a href="{{ '/blogs' | relative_url }}" style="padding: 1.25rem; background: white; border-radius: 8px; text-decoration: none; color: var(--primary-color); border-left: 4px solid #9945ff; transition: all 0.2s; box-shadow: var(--shadow-sm);" onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='var(--shadow)';" onmouseout="this.style.transform='none'; this.style.boxShadow='var(--shadow-sm)';">
                        <div style="font-weight: 700; margin-bottom: 0.3rem;">✍️ All Posts</div>
                        <div style="font-size: 0.9rem; color: var(--light-text);">Browse every article</div>
                    </a>
                </div>
            </div>
        </div>
    </div>
    <div id="activity" class="hf-panel">
        <div class="activity-list">
            <div class="col">
                <h3>Recent Projects</h3>
                <div class="projects-list">
                    {% for project in site.projects limit:3 %}
                    <div class="project-card">
                        <h3><a href="{{ project.url }}">{{ project.title }}</a></h3>
                        {% if project.description %}<p>{{ project.description }}</p>{% endif %}
                    </div>
                    {% endfor %}
                </div>
            </div>
            <div class="col">
                <h3>Recent Posts</h3>
                <ul>
                    {% for post in site.posts limit:5 %}
                    <li class="home-post-item"><a href="{{ post.url }}">{{ post.title }}</a> - <time>{{ post.date | date: "%b %d, %Y" }}</time></li>
                    {% endfor %}
                </ul>
            </div>
        </div>
    </div>
</div>



## 📝 Latest Blog Posts

{% for post in site.posts limit: 3 %}
- **[{{ post.title }}]({{ post.url }})** - <time>{{ post.date | date: "%B %d, %Y" }}</time>
{% endfor %}

<a href="{{ '/blogs' | relative_url }}" class="btn-crosslink" style="display: inline-flex; margin-top: 1rem;"><span style="font-size: 1.2rem; margin-right: 0.5rem;">📖</span> Read More Posts</a>


## 📚 Learning Journey

Explore topic-wise paths and quick intros below.

<div class="projects-list">
    <div class="project-card">
        <h3><a href="{{ '/learning/programming-language/' | relative_url }}">Explore Programming Languages</a></h3>
        <p>All about C, C++, Java, Python and other language basics.</p>
    </div>
    <div class="project-card">
        <h3><a href="{{ '/learning/dsa/' | relative_url }}">Data Structures & Algorithms</a></h3>
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
    <div class="project-card">
                <h3><a href="{{ '/learning/data-plane/' | relative_url }}">Data Plane Development</a></h3>
                <p>Data Plane Products Development and projects.</p>
    </div>
</div>

<a href="{{ '/learning' | relative_url }}" class="btn-crosslink" style="display: inline-flex; margin-top: 1rem;"><span style="font-size: 1.2rem; margin-right: 0.5rem;">📚</span> Explore Full Learning Hub</a>

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


<a href="{{ '/projects' | relative_url }}" class="btn-crosslink" style="display: inline-flex; margin-top: 1rem;"><span style="font-size: 1.2rem; margin-right: 0.5rem;">🚀</span> View All Projects</a>


## 💡 About This Site

This portfolio showcases my journey in programming, learning data structures & Algorithm during my Computer Science Engineering. Feel free to explore my work and [learn more about me]({{ '/about' | relative_url }}).

