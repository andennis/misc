<p> The mattermost operator (v1.20.1) was copied from</p>

> https://github.com/mattermost/mattermost-operator/blob/v1.20.1/docs/mattermost-operator/mattermost-operator.yaml
<p>
The image version/tag was set to v1.20.1.<br>
The image location was changes to the local docker registry "registry.local"
</p>

> image: registry.local/mattermost/mattermost-operator:v1.20.1

<p>The local docker registry requires authentication. The <em>docker-registry</em> secret must be added</p>

> kubectl create secret docker-registry registry-local-client \
> --docker-server=registry.local \
> --docker-username=<user name> \
> --docker-password=<password> \
> -n mattermost-operator

The authentication secret must be referenced in mattermost-operator deployment

>      imagePullSecrets:
>        - name: registry-local-client
