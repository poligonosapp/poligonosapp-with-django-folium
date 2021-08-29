# Object oriented:
    # Get the repository first
    r = cloud.workspaces.get(workspace).repositories.get(repository)

    # Get all Pipelines results for repository
    r.pipelines.each()

    # Trigger default Pipeline on the latest revision of the master branch
    r.pipelines.trigger()

    # Trigger default Pipeline on the latest revision of the develop branch
    r.pipelines.trigger(branch="develop")

    # Trigger default Pipeline on a specific revision of the develop branch
    r.pipelines.trigger(branch="develop", revision="<40-char hash>")

    # Trigger specific Pipeline on a specific revision of the master branch
    r.pipelines.trigger(revision="<40-char hash>", name="style-check")

    # Get specific Pipeline by UUID
    pl = r.pipelines.get("{7d6c327d-6336-4721-bfeb-c24caf25045c}")

    # Stop specific Pipeline by UUID
    pl.stop()

    # Get steps of Pipeline specified by UUID
    pl.steps()

    # Get step of Pipeline specified by UUIDs
    s = pl.step("{56d2d8af-6526-4813-a22c-733ec6ecabf3}")

    # Get log of step of Pipeline specified by UUIDs
    s.log()

# or function oriented:
    # Get most recent Pipelines results for repository
    bitbucket.get_pipelines(workspace, repository)

    # Trigger default Pipeline on the latest revision of the master branch
    bitbucket.trigger_pipeline(workspace, repository)

    # Trigger default Pipeline on the latest revision of the develop branch
    bitbucket.trigger_pipeline(workspace, repository, branch="develop")

    # Trigger default Pipeline on a specific revision of the develop branch
    bitbucket.trigger_pipeline(workspace, repository, branch="develop", revision="<40-char hash>")

    # Trigger specific Pipeline on a specific revision of the master branch
    bitbucket.trigger_pipeline(workspace, repository, revision="<40-char hash>", name="style-check")

    # Get specific Pipeline by UUID
    bitbucket.get_pipeline(workspace, repository, "{7d6c327d-6336-4721-bfeb-c24caf25045c}")

    # Stop specific Pipeline by UUID
    bitbucket.stop_pipeline(workspace, repository, "{7d6c327d-6336-4721-bfeb-c24caf25045c}")

    # Get steps of Pipeline specified by UUID
    bitbucket.get_pipeline_steps(workspace, repository, "{7d6c327d-6336-4721-bfeb-c24caf25045c}")

    # Get step of Pipeline specified by UUIDs
    bitbucket.get_pipeline_step(workspace, repository, "{7d6c327d-6336-4721-bfeb-c24caf25045c}", "{56d2d8af-6526-4813-a22c-733ec6ecabf3}")

    # Get log of step of Pipeline specified by UUIDs
    bitbucket.get_pipeline_step_log(workspace, repository, "{7d6c327d-6336-4721-bfeb-c24caf25045c}", "{56d2d8af-6526-4813-a22c-733ec6ecabf3}")