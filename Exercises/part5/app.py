from flask import Flask, render_template

app = Flask(__name__)



PERSONAL_INFO = {
    'name': 'Priyesh Kathe',
    'title': 'Full Stack Web Developer',
    'bio': 'A passionate developer learning Flask and web development.',
    'email': 'priyeshkathe@gmail.com',
    'github': 'https://github.com/priyeshkathe',
    'linkedin': 'https://linkedin.com/in/priyesh-kathe-7457a5361',
}

SKILLS = [
    {'name': 'Python', 'level': 80},
    {'name': 'HTML/CSS', 'level': 90},
    {'name': 'Flask', 'level': 60},
    {'name': 'JavaScript', 'level': 50},
    {'name': 'SQL', 'level': 45},
]

PROJECTS = [
    {
        'id': 1,
        'name': 'Personal Portfolio Website',
        'description': 'A personal portfolio website built using Flask with dynamic routing, template inheritance, and responsive UI to showcase skills and projects.',
        'tech': ['Python', 'Flask', 'HTML', 'CSS', 'Jinja2'],
        'status': 'Completed'
    },
    {
        'id': 2,
        'name': 'Spotify Frontend Clone',
        'description': 'A frontend clone of Spotify focusing on UI design, layouts, and user experience similar to the original application.',
        'tech': ['HTML', 'CSS', 'JavaScript'],
        'status': 'In Progress'
    },
    {
        'id': 3,
        'name': 'Weather Dashboard',
        'description': 'A web dashboard that fetches and displays real-time weather data from an external API.',
        'tech': ['Python', 'Flask', 'API'],
        'status': 'Planned'
    }
]


# ROUTES


@app.route('/')
def home():
    return render_template('index.html', info=PERSONAL_INFO)


@app.route('/about')
def about():
    return render_template('about.html', info=PERSONAL_INFO, skills=SKILLS)


@app.route('/projects')
def projects():
    return render_template('projects.html', info=PERSONAL_INFO, projects=PROJECTS)


@app.route('/project/<int:project_id>')  # Dynamic route for individual project
def project_detail(project_id):
    project = None
    for p in PROJECTS:
        if p['id'] == project_id:
            project = p
            break
    return render_template('project_detail.html', info=PERSONAL_INFO, project=project, project_id=project_id)


@app.route('/contact')
def contact():
    return render_template('contact.html', info=PERSONAL_INFO)


if __name__ == '__main__':
    app.run(debug=True)



# Exercise 5.2: Add a new page
#   - Create a /blog route
#   - Add blog posts data structure
#   - Create blog.html template
#
# Exercise 5.3: Enhance the styling
#   - Modify static/style.css
#   - Add your own color scheme
#   - Make it responsive for mobile
#
# Exercise 5.4: Add more dynamic features
#   - Create a /skill/<skill_name> route
#   - Show projects that use that skill
#
# =============================================================================
