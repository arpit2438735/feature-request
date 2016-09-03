import templateUrl from './new-feature-request.html';

class featureRequestController {
    constructor(FeatureRequestApiService, $uibModal) {
        this.modal = $uibModal;
        FeatureRequestApiService.getFeatureRequestList().then(() => {
            this.featureRequestList = FeatureRequestApiService.model;
        });
    }

    openRequestFormModal() {
        this.modal.open({
            templateUrl,
            controllerAs: 'ctrl'
        });
    }
}

featureRequestController.$inject = ['FeatureRequestApiService', '$uibModal'];

export default featureRequestController;