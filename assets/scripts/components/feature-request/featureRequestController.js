import templateUrl from './new-feature-request.html';

class featureRequestController {
    constructor(FeatureRequestApiService, $uibModal, $http, $scope, $filter) {
        this.modal = $uibModal;
        this.$scope = $scope;
        this.$filter = $filter;
        this.modalInstance = null;
        this.FeatureRequestApiService = FeatureRequestApiService;
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

        this.modalInstance = this.modal.open({
            templateUrl,
            controllerAs: 'ctrl',
            scope: this.$scope
        });
    }

    closeModal() {
        if(!this.modalInstance) {
            return;
        }
        this.modalInstance.dismiss();
    }

    saveNewFeature(form, featureRequest) {
        if(!form.$valid|| !this.modalInstance) {
            return
        }

        let newFeatureRequest = angular.copy(featureRequest);
        newFeatureRequest.target_date = this.$filter('date')(newFeatureRequest.target_date, 'yyyy-MM-dd');

        this.FeatureRequestApiService.addNewFeatureRequest(newFeatureRequest).then(() => {
            this.featureRequestList = this.FeatureRequestApiService.model;
        });

        this.modalInstance.dismiss();
    }
}

featureRequestController.$inject = ['FeatureRequestApiService', '$uibModal', '$http', '$scope', '$filter'];

export default featureRequestController;