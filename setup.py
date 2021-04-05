import setuptools


setuptools.setup(
    name = "u-slash",
    version = "0.1",
    py_modules = ["u_slash"],
    install_requires = ["click", "praw", "requests"],
    entry_points = """
        [console_scripts]
        u-slash=u_slash:u_slash
    """
)
