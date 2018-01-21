from setuptools import setup, find_packages

setup(
    name='chatflow',
    version='0.0.1',
    description='Python wrapper for ChatFlow.ai',
    license='MIT',
    maintainer='ByungWook Kang',
    maintainer_email='lesimor@naver.com',
    url='https://github.com/lesimor/chatflow_pkg',
    install_requires=['requests'],
    packages=find_packages(exclude=['tests']),
    long_description=open('README.md').read(),
    keywords=['chatflow', 'chatbot'],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)
