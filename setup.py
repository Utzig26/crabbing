from setuptools import setup, find_packages

setup(
    name="crabbing",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'crabbing = crab.crabbing:run_crabbing',
        ]
    }
)