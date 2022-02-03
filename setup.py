from setuptools import setup, find_packages
# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent

VERSION = '0.0.4'
DESCRIPTION = 'A Voicemaker.in simple API interface'
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

# Setting up
setup(
        name="voicemaker", 
        version=VERSION,
        author="Adrian Castro",
        author_email="<adrian.d.castro.t@gmail.com>",
        url='https://github.com/IAL32/voicemaker',
        license='MIT',
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        packages=find_packages(),
        install_requires=["requests>=2.2"], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'tts', 'voicemaker', 'api'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
