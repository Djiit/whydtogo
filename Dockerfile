FROM python:3-onbuild

MAINTAINER Julien Tanay <julien.tanay@gmail.com>

CMD ["--help"]

ENTRYPOINT ["python whydtogo/__init__.py"]
