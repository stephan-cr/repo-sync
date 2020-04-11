Repo-sync
=========

Keep repositories in sync with upstream.

How to install
--------------

.. code:: shell

   pip install -e git+https://github.com/stephan-cr/repo-sync#egg=repo-sync

Supported Version Control Systems
---------------------------------

+-------------+-----------+
| VCS         | repo-sync |
|             | type      |
+=============+===========+
| Git_        | git       |
+-------------+-----------+
| Mercurial_  | hg        |
+-------------+-----------+
| Subversion_ | svn       |
+-------------+-----------+

.. _Git: https://git-scm.com/
.. _Mercurial: https://www.mercurial-scm.org/
.. _Subversion: https://subversion.apache.org/

Configuration File Structure
----------------------------

A configuration file in `$XDG_CONFIG_HOME/sync-repos.conf` is required
and is structured as follows:

.. code-block:: json

   [
       {
           "repo-type": "git",
           "dir": "/home/xxx"
       },
       {
           "repo-type": "hg",
           "dir": "/home/yyy"
       }
   ]

XDG_ is used to locate configuration files. If `$XDG_CONFIG_HOME` is
not set, it defaults to `$HOME/.config`.

.. _XDG: https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html
