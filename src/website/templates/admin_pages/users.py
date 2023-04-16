{% extends 'layout/base.html' %}


{% block content %}
    <link rel='stylesheet' href='/static/css/users.html'>

    <table>
        <tr>
            <th>Email</th>
            <th>Display Name</th>
            <th>Role</th>
        </tr>

        {% for user in users %}
            <tr>
                <td>user['email']</td>
                <td>user['display_name']</td>
                <td>user['role']</td>
            </tr>
        {% endfor %}
{% endblock %}
