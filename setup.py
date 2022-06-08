from pathlib import Path
from setuptools import setup, find_packages

DESCRIPTION = (
    "Boilerplate Flask API with Flask-RESTx"
)
APP_ROOT = Path(__file__).parent
README = (APP_ROOT / "README.md").read_text()
AUTHOR = "Hector Latorre"
AUTHOR_EMAIL = "hector.latorre23@gmail.com"
PROJECT_URLS = {
    "Source Code": "https://github.com/hlatorreg/Talana",
}
INSTALL_REQUIRES = [
    "Flask==2.0.1",
    "flask-restx",
    "python-dateutil",
    "python-dotenv",
    "requests",
    "urllib3",
    "jinja2<3.1.0",
    "werkzeug==2.0.3",
]
EXTRAS_REQUIRE = {
    "dev": [
        "black",
        "pre-commit",
        "pydocstyle"
    ]
}

setup(
    name="talana-kombat",
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    version="0.1",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    license="MIT",
    url="https://github.com/hlatorreg/Talana",
    project_urls=PROJECT_URLS,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
)
