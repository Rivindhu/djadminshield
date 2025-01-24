from setuptools import setup, find_packages

setup(
    name="djadminshield",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requirements=[
        'django>=5.0',
    ],
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
)