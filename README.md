# heroku-pipenv-link-bug

Example app to showcase the bug reported on https://github.com/heroku/heroku-buildpack-python/issues/687


# Steps to recreate

1. Create a new directory and `cd` into it.
2. Copy over the `setup.py` file.
3. Copy over the `src/pipenvbug/__init__.py` file.
4. Copy over the `Procfile` file.
5. Copy over the `production.ini` file.
6. `pipenv install -e .`
7. `pipenv install pyramid`
8. `pipenv install gunicorn`


# Exercise the bug

1. Create a new Heroku app (`pipenvbug` in my case)
2. `git push heroku master`
3. Get the following error:

    ```
    heroku-pipenv-link-bug (master)$ git push heroku master
    Counting objects: 12, done.
    Delta compression using up to 8 threads.
    Compressing objects: 100% (8/8), done.
    Writing objects: 100% (12/12), 4.16 KiB | 2.08 MiB/s, done.
    Total 12 (delta 0), reused 0 (delta 0)
    remote: Compressing source files... done.
    remote: Building source:
    remote:
    remote: -----> Python app detected
    remote: -----> Installing python-3.7.2
    remote: -----> Installing pip
    remote: -----> Installing dependencies with Pipenv 2018.5.18…
    remote:        Installing -e .…
    remote:        Obtaining file:///tmp/build_eb2a08e3547356f962fb226d6ffc15ae
    remote:        Installing collected packages: pipenvbug
    remote:          Running setup.py develop for pipenvbug
    remote:        Successfully installed pipenvbug
    remote:
    remote:        Adding -e . to Pipfile's [packages]…
    remote:        Creating a virtualenv for this project…
    remote:        Using /app/.heroku/python/bin/python (3.7.2) to create virtualenv…
    remote:        Already using interpreter /app/.heroku/python/bin/python
    remote:        Using base prefix '/app/.heroku/python'
    remote:        New python executable in /app/.local/share/virtualenvs/build_eb2a08e3547356f962fb226d6ffc15ae-yRNJIowl/bin/python
    remote:        Installing setuptools, pip, wheel...
    remote:        done.
    remote:
    remote:        Virtualenv location: /app/.local/share/virtualenvs/build_eb2a08e3547356f962fb226d6ffc15ae-yRNJIowl
    remote:        Your Pipfile.lock (11aa32) is out of date. Expected: (c9675e).
    remote:        Aborting deploy.
    remote:  !     Push rejected, failed to compile Python app.
    remote:
    remote:  !     Push failed
    remote: Verifying deploy...
    remote:
    remote: !   Push rejected to pipenvbug.
    remote:
    To https://git.heroku.com/pipenvbug.git
     ! [remote rejected] master -> master (pre-receive hook declined)
    error: failed to push some refs to 'https://git.heroku.com/pipenvbug.git'
    ```
4. Fix the error by [replacing `pipenvbug` in Pipfile with `e1839a8`](https://github.com/zupo/heroku-pipenv-link-bug/commit/5c8c6f9a462a6b2ad45f14b8c15d3a01f5c5df24). Not sure why exactly this is needed, but there are [a ton of bugs reported](https://github.com/pypa/pipenv/search?q=e1839a8&type=Issues) around it.
5. `pipenv lock && git add Pipfile* && git ci && git push heroku master`
6. The build is now successful, yay!

    ```
    heroku-pipenv-link-bug (master)$ git push heroku master
    Counting objects: 17, done.
    Delta compression using up to 8 threads.
    Compressing objects: 100% (13/13), done.
    Writing objects: 100% (17/17), 4.76 KiB | 2.38 MiB/s, done.
    Total 17 (delta 2), reused 0 (delta 0)
    remote: Compressing source files... done.
    remote: Building source:
    remote:
    remote: -----> Python app detected
    remote: -----> Installing python-3.7.2
    remote: -----> Installing pip
    remote: -----> Installing dependencies with Pipenv 2018.5.18…
    remote:        Installing -e .…
    remote:        Obtaining file:///tmp/build_9c6b10f93e686a820ef57e2dd20265d1
    remote:        Installing collected packages: pipenvbug
    remote:          Running setup.py develop for pipenvbug
    remote:        Successfully installed pipenvbug
    remote:
    remote:        Adding -e . to Pipfile's [packages]…
    remote:        Creating a virtualenv for this project…
    remote:        Using /app/.heroku/python/bin/python (3.7.2) to create virtualenv…
    remote:        Already using interpreter /app/.heroku/python/bin/python
    remote:        Using base prefix '/app/.heroku/python'
    remote:        New python executable in /app/.local/share/virtualenvs/build_9c6b10f93e686a820ef57e2dd20265d1-KXinJ-YT/bin/python
    remote:        Installing setuptools, pip, wheel...
    remote:        done.
    remote:
    remote:        Virtualenv location: /app/.local/share/virtualenvs/build_9c6b10f93e686a820ef57e2dd20265d1-KXinJ-YT
    remote:        Installing dependencies from Pipfile.lock (e7b348)…
    remote:        An error occurred while installing zope.interface==4.6.0! Will try again.
    remote:        Installing initially–failed dependencies…
    remote:        Success installing zope.interface==4.6.0!
    remote: -----> Installing SQLite3
    remote: -----> Discovering process types
    remote:        Procfile declares types -> web
    remote:
    remote: -----> Compressing...
    remote:        Done: 58.7M
    remote: -----> Launching...
    remote:        Released v3
    remote:        https://pipenvbug.herokuapp.com/ deployed to Heroku
    remote:
    remote: Verifying deploy... done.
    To https://git.heroku.com/pipenvbug.git
     * [new branch]      master -> master
     ```
7. OK, now we do a change to the app and push the commit to Heroku: `sed -i -e "s/works/workz/" src/pipenvbug/__init__.py && git add src/pipenvbug/__init__.py && git ci && git push heroku master`.
8. The build passes:
    ```
    heroku-pipenv-link-bug (master)$ git push heroku master
    Counting objects: 5, done.
    Delta compression using up to 8 threads.
    Compressing objects: 100% (3/3), done.
    Writing objects: 100% (5/5), 376 bytes | 376.00 KiB/s, done.
    Total 5 (delta 2), reused 0 (delta 0)
    remote: Compressing source files... done.
    remote: Building source:
    remote:
    remote: -----> Python app detected
    remote:        Skipping installation, as Pipfile.lock hasn't changed since last deploy.
    remote: -----> Discovering process types
    remote:        Procfile declares types -> web
    remote:
    remote: -----> Compressing...
    remote:        Done: 58.8M
    remote: -----> Launching...
    remote:        Released v4
    remote:        https://pipenvbug.herokuapp.com/ deployed to Heroku
    remote:
    remote: Verifying deploy... done.
    To https://git.heroku.com/pipenvbug.git
       5c8c6f9..4ff4e09  master -> master
    ```
9. However, the app does not start:
    ```
    2019-02-18T10:10:20.946962+00:00 app[web.1]: [2019-02-18 10:10:20 +0000] [4] [INFO] Starting gunicorn 19.9.0
    2019-02-18T10:10:20.947915+00:00 app[web.1]: [2019-02-18 10:10:20 +0000] [4] [INFO] Listening at: http://0.0.0.0:23298 (4)
    2019-02-18T10:10:20.948115+00:00 app[web.1]: [2019-02-18 10:10:20 +0000] [4] [INFO] Using worker: sync
    2019-02-18T10:10:20.956139+00:00 app[web.1]: [2019-02-18 10:10:20 +0000] [10] [INFO] Booting worker with pid: 10
    2019-02-18T10:10:20.990249+00:00 app[web.1]: [2019-02-18 10:10:20 +0000] [11] [INFO] Booting worker with pid: 11
    2019-02-18T10:10:20.993764+00:00 app[web.1]: [2019-02-18 10:10:20 +0000] [10] [ERROR] Exception in worker process
    2019-02-18T10:10:20.993767+00:00 app[web.1]: Traceback (most recent call last):
    2019-02-18T10:10:20.993769+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/gunicorn/arbiter.py", line 583, in spawn_worker
    2019-02-18T10:10:20.993771+00:00 app[web.1]: worker.init_process()
    2019-02-18T10:10:20.993773+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/gunicorn/workers/base.py", line 129, in init_process
    2019-02-18T10:10:20.993774+00:00 app[web.1]: self.load_wsgi()
    2019-02-18T10:10:20.993776+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/gunicorn/workers/base.py", line 138, in load_wsgi
    2019-02-18T10:10:20.993777+00:00 app[web.1]: self.wsgi = self.app.wsgi()
    2019-02-18T10:10:20.993779+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/gunicorn/app/base.py", line 67, in wsgi
    2019-02-18T10:10:20.993781+00:00 app[web.1]: self.callable = self.load()
    2019-02-18T10:10:20.993782+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/gunicorn/app/wsgiapp.py", line 50, in load
    2019-02-18T10:10:20.993784+00:00 app[web.1]: return self.load_pasteapp()
    2019-02-18T10:10:20.993785+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/gunicorn/app/wsgiapp.py", line 46, in load_pasteapp
    2019-02-18T10:10:20.993787+00:00 app[web.1]: return load_pasteapp(self.cfgurl, self.relpath, global_conf=self.cfg.paste_global_conf)
    2019-02-18T10:10:20.993788+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/gunicorn/app/pasterapp.py", line 71, in load_pasteapp
    2019-02-18T10:10:20.993790+00:00 app[web.1]: global_conf=global_conf)
    2019-02-18T10:10:20.993791+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/paste/deploy/loadwsgi.py", line 253, in loadapp
    2019-02-18T10:10:20.993793+00:00 app[web.1]: return loadobj(APP, uri, name=name, **kw)
    2019-02-18T10:10:20.993795+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/paste/deploy/loadwsgi.py", line 277, in loadobj
    2019-02-18T10:10:20.993797+00:00 app[web.1]: global_conf=global_conf)
    2019-02-18T10:10:20.993798+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/paste/deploy/loadwsgi.py", line 302, in loadcontext
    2019-02-18T10:10:20.993800+00:00 app[web.1]: global_conf=global_conf)
    2019-02-18T10:10:20.993801+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/paste/deploy/loadwsgi.py", line 326, in _loadconfig
    2019-02-18T10:10:20.993803+00:00 app[web.1]: return loader.get_context(object_type, name, global_conf)
    2019-02-18T10:10:20.993805+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/paste/deploy/loadwsgi.py", line 459, in get_context
    2019-02-18T10:10:20.993807+00:00 app[web.1]: section)
    2019-02-18T10:10:20.993808+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/paste/deploy/loadwsgi.py", line 481, in _context_from_use
    2019-02-18T10:10:20.993810+00:00 app[web.1]: object_type, name=use, global_conf=global_conf)
    2019-02-18T10:10:20.993812+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/paste/deploy/loadwsgi.py", line 412, in get_context
    2019-02-18T10:10:20.993813+00:00 app[web.1]: global_conf=global_conf)
    2019-02-18T10:10:20.993815+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/paste/deploy/loadwsgi.py", line 302, in loadcontext
    2019-02-18T10:10:20.993817+00:00 app[web.1]: global_conf=global_conf)
    2019-02-18T10:10:20.993818+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/paste/deploy/loadwsgi.py", line 334, in _loadegg
    2019-02-18T10:10:20.993820+00:00 app[web.1]: return loader.get_context(object_type, name, global_conf)
    2019-02-18T10:10:20.993821+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/paste/deploy/loadwsgi.py", line 625, in get_context
    2019-02-18T10:10:20.993823+00:00 app[web.1]: object_type, name=name)
    2019-02-18T10:10:20.993824+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/paste/deploy/loadwsgi.py", line 645, in find_egg_entry_point
    2019-02-18T10:10:20.993826+00:00 app[web.1]: pkg_resources.require(self.spec)
    2019-02-18T10:10:20.993828+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/pkg_resources/__init__.py", line 892, in require
    2019-02-18T10:10:20.993829+00:00 app[web.1]: needed = self.resolve(parse_requirements(requirements))
    2019-02-18T10:10:20.993831+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.7/site-packages/pkg_resources/__init__.py", line 778, in resolve
    2019-02-18T10:10:20.993832+00:00 app[web.1]: raise DistributionNotFound(req, requirers)
    2019-02-18T10:10:20.993834+00:00 app[web.1]: pkg_resources.DistributionNotFound: The 'pipenvbug' distribution was not found and is required by the application
    ```

# Workarounds

There are two:

1. Before each `git push heroku master` purge the Heroku build cache which makes the pipenv run in a clean directory and all required files are created.
2. Run the following script using the [heroku-buildpack-shell](https://github.com/niteoweb/heroku-buildpack-shell) buildpack (set as the last buildpack):

    ```bash
    if [[ -d /app/src/happy.egg-info ]]
    then
        echo "Local package is linked to site-packages, skip deploy."
    else
        echo "Local package is not linked to site-package, creating egg."
        pipenv install --system --deploy
    fi
    echo "/app/src" > /app/.heroku/python/lib/python3.7/site-packages/happy.egg-link
    ```
