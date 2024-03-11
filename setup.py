from setuptools import setup, find_packages

setup(
    name="gmail-label-email-processor",
    version="1.0.1",
    author="SokinjoNS",
    author_email="sokinjo.155@gmail.com",
    description="A comprehensive toolkit for processing emails via Gmail API, including authentication, label management, message processing, and data exporting.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SokinjoNS/gmail-label-email-processor",
    project_urls":{"Source":"https://github.com/SokinjoNS/gmail-label-email-processor"},
    packages=find_packages(),
    install_requires=[
        'google-api-python-client>=2.88.0',
        'google-auth-httplib2>=0.1.0',
        'google-auth-oauthlib>=1.0.0',
        'gmail_api_auth==0.1.1',
        'gmail_label_manager==0.1.1',
        'gmail_message_processor==0.1.1',
        'data_exporter==0.1.1', 

    ],
    entry_points={
        'console_scripts': [
            'gmail-processor=gmail_main_sc:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
