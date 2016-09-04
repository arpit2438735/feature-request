import templateUrl from './new-feature-request.html';

class featureRequestController {
    constructor(FeatureRequestApiService, $uibModal, $http) {
        this.modal = $uibModal;
        FeatureRequestApiService.getFeatureRequestList().then(() => {
            this.featureRequestList = FeatureRequestApiService.model;
        });

        $http.get('/api/client/').then((response) => {
            this.clientList = response.data.clients;
        });

        $http.get('/api/product/').then((response) => {
            this.productList = response.data.products;
        });
    }

    openRequestFormModal() {
        this.modal.open({
            templateUrl,
            controllerAs: 'ctrl',
            scope: this
        });
    }
}

featureRequestController.$inject = ['FeatureRequestApiService', '$uibModal', '$http'];

export default featureRequestController;