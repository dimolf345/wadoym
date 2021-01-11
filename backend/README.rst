wadoym
==============================

What do you mean?

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django



Deployment
----------
Local
^^^^^

To deploy the app locally (for testing/development), you will need to:
#. Create a virtualenv (basic).
#. Install application package as develop.
   .. code-block:: bash
        python setup.py develop
#. Serve the application itself:
   .. code-block:: bash
        export FALCON_SETTINGS_MODULE=wadoym.settings.local
        gunicorn wadoym.app:app --bind:127.0.0.1:8000 --reload

   Or
   
   .. code-block:: bash
        export FALCON_SETTINGS_MODULE=wadoym.settings.local
        python wadoym/app.py

It is very important to set the environment before serving the app or it won't work.



Docker
^^^^^^

To tun docker container application you just need to run:

