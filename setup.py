"""Setup file."""
import re
from typing import List

import setuptools


def get_requirements(filename: str = "requirements.txt") -> List[str]:
    """Get the requirements from a file."""
    with open(filename, encoding="utf-8") as file:
        content = file.read().splitlines()
        for line in content:
            if line.startswith("#"):
                content.remove(line)
            elif line.startswith("-r"):
                content.remove(line)
                content.extend(get_requirements(line[3:]))
    return content


requirements = get_requirements()

# Version Info
version = ""
with open("bftools/__init__.py", encoding="utf-8") as f:

    search = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    )

    if search is not None:
        version = search.group(1)

    else:
        raise RuntimeError("Could not grab version string")

if not version:
    raise RuntimeError("version is not set")

if version.endswith(("a", "b", "rc")):
    # append version identifier based on commit count
    try:
        import subprocess

        with subprocess.Popen(
            ["git", "rev-list", "--count", "HEAD"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ) as p:
            out, err = p.communicate()
        if out:
            version += out.decode("utf-8").strip()
        with subprocess.Popen(
            ["git", "rev-parse", "--short", "HEAD"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ) as p:
            out, err = p.communicate()
        if out:
            version += f"+g{out.decode('utf-8').strip()}"
    except Exception:  # pylint: disable=broad-except
        pass

with open("README.rst", encoding="utf-8") as fh:
    long_description = fh.read()

packages = [
    "bftools",
]

extras_require = {
    "docs": get_requirements("docs/requirements.txt"),
    "dev": get_requirements("requirements-dev.txt"),
    "minify": [
        "python-minifier<2.7",
    ],
}

extras_require["all"] = list(set(sum(extras_require.values(), [])))


setuptools.setup(
    name="bftools",
    version=version,
    author="BobDotCom",
    author_email="bobdotcomgt@gmail.com",
    description="A brainfuck toolbox for python.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/BobDotCom/bftools",
    download_url="https://github.com/BobDotCom/bftools/releases",
    packages=packages,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
    install_requires=requirements,
    extras_require=extras_require,
    python_requires=">=3.7",
    license="MIT",
    project_urls={
        # TODO: Add changelog
        # "Changelog": "https://github.com/BobDotCom/bftools/blob/main/CHANGELOG.rst",
        "Documentation": "https://bftools.rtfd.io/",
        "Source": "https://github.com/BobDotCom/bftools",
        "Tracker": "https://github.com/BobDotCom/bftools/issues",
    },
    include_package_data=True,
)
