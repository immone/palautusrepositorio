from urllib import request
from project import Project
import rtoml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        content2 = rtoml.load(content)
        deps = content2["tool"]["poetry"]["dependencies"]
        devdeps	 = content2["tool"]["poetry"]["dev-dependencies"]
        name = content2["tool"]["poetry"]["name"]
        desc = content2["tool"]["poetry"]["description"]
        ##print("asDASADSDSADASDDSDDSAd", content2)
        ##print(content2["tool"]["poetry"]["dependencies"]["tool.poetry.dependencies"])

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, deps, devdeps)
