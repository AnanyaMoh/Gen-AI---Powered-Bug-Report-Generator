from flask import Flask, request, jsonify
from generator.ai_engine import generate_report
from github_integration.github_api import create_github_issue

app = Flask(_name_)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    log = data.get('error_log', '')
    format_type = data.get('output_format', 'markdown')

    report = generate_report(log)

    if format_type == 'github':
        issue_url = create_github_issue(report)
        report['github_issue_url'] = issue_url

    return jsonify(report)

if _name_ == '_main_':
    app.run(debug=True)
