A utility to quickly get versions of microservices currently deployed to the environment in the current kubernetes cluster context.

The kube_config.cfg file must either contain the current kubectl config or be a symbolic link to a valid kubectl config.

To run:

- Specify parameters in the main.py file:

project_namespace_name = "" // namespace name

get_data_from = 'deployment' // where to get information from (from deployments or pods); by default, as you can see, it is taken from deployments.

- Install dependencies: pip install -r requirements.txt
