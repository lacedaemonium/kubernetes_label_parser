from kubernetes import client, config

kube_config_file = "kube_config.cfg"
config.load_kube_config(kube_config_file)
kube_client = client.AppsV1Api()
project_namespace_name = ""  # имя неймспейса
get_data_from = 'deployment' # откуда брать данные: deployment (из деплойментов) либо pod (из подов)


if get_data_from == 'deployment':
    print(f'take data from {get_data_from}')
    # step 1: get list of all deployments
    def get_list_of_deployments_in_namespace(namespace):
        deployments_list = []
        resp = kube_client.list_namespaced_deployment(namespace)
        for i in resp.items:
            deployments_list.append(i.metadata.name)
        return deployments_list

    deployments_list = get_list_of_deployments_in_namespace(project_namespace_name)

    # # step 2: iterate all deployments and get label version
    def get_version_from_deployment(deployment, namespace):
        deployments_list = []
        resp = kube_client.read_namespaced_deployment_status(deployment, namespace)
        version = (resp.metadata.labels['version'])
        return {'deployment': deployment, 'version': version}

    for deployment in deployments_list:
        info = get_version_from_deployment(deployment, project_namespace_name)
        print(info)

elif get_data_from == 'pods':
    print(f'take data from {get_data_from}')
    def get_pods_info_from_pods(namespace):
        pods_data = []
        v1 = client.CoreV1Api()
        pod_list = v1.list_namespaced_pod(namespace)
        for pod in pod_list.items:
            pods_data.append({'pod_name': pod.metadata.name, 'pod_label_version': pod.metadata.labels['version']})
            # print("%s %s" % (pod.metadata.name, pod.metadata.labels['version']))
        return pods_data

    pods_data = get_pods_info_from_pods(project_namespace_name)
    #print(pods_data)

    # step 1: get list of all deployments
    def get_list_of_deployments_in_namespace(namespace):
        deployments_list = []
        resp = kube_client.list_namespaced_deployment(namespace)
        for i in resp.items:
            deployments_list.append(i.metadata.name)
        return deployments_list

    deployments_list = get_list_of_deployments_in_namespace(project_namespace_name)

    # step 2: iterate all deployments and get env
    def get_env_from_deployment(deployment, namespace):
        deployments_list = []
        resp = kube_client.read_namespaced_deployment_status(deployment, namespace)
        name = resp.spec.template.spec.containers[0].env[0].name
        value = resp.spec.template.spec.containers[0].env[0].value
        return ({'name': name, 'value': value})
        #print(name + value)

    for deployment in deployments_list:
        info = get_env_from_deployment(deployment, project_namespace_name)
        print(info)
