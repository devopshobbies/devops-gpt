export interface ArgocdBody {
  argocd_application: {
    sync_policy: {
      auto_prune: boolean;
      self_heal: boolean;
    };
  } | null;
  argocd_repository: boolean;
  application_depends_repository: boolean;
}

export interface ArgocdResponse {
  output: 'string';
}
