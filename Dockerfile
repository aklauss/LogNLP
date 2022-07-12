FROM gitpod/gitpod/workspace-python-3.8

USER gitpod
ENV PYTHONUSERBASE=/workspace/.pip-modules
ENV PATH=$PYTHONUSERBASE/bin:$PATH
ENV PIP_USER=yes 