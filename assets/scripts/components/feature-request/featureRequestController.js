import templateUrl from './new-feature-request.html';

const convertToObject = (dataArray, key) => {
    const newObject = {};

    dataArray.forEach((data, index)=> {
        newObject[data[key]] = data;
    });

    return newObject;
};

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
            this.clientModel = convertToObject(response.data.clients, 'name');
        });

        $http.get('/api/product/').then((response) => {
            this.productModel = convertToObject(response.data.products, 'name');
        });
    }

    openRequestFormModal(showFeatureRequestValue) {

        this.featureRequest = angular.copy(showFeatureRequestValue);

        if (this.featureRequest) {
            this.featureRequest.target_date = new Date(this.featureRequest.target_date);
            this.featureRequest.client_id = this.clientModel[this.featureRequest.client_name].id;
            this.featureRequest.product_id = this.productModel[this.featureRequest.product_area].id;
        }

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

    saveNewFeature(form, productId) {
        if(!form.$valid|| !this.modalInstance) {
            return
        }

        let newFeatureRequest = angular.copy(this.featureRequest);
        newFeatureRequest.target_date = this.$filter('date')(newFeatureRequest.target_date, 'yyyy-MM-dd');

        if (productId) {
            this.FeatureRequestApiService.updateFeatureRequest(productId, newFeatureRequest);
        } else {
            this.FeatureRequestApiService.addNewFeatureRequest(newFeatureRequest).then(() => {
                this.featureRequestList = this.FeatureRequestApiService.model;
            });
        }


        this.modalInstance.dismiss();
    }

    openModelWithCurrentFeatureRequestValue(index) {
        if(index === null || index === undefined) {
            return;
        }

        this.openRequestFormModal(this.featureRequestList[index]);
    }
}

featureRequestController.$inject = ['FeatureRequestApiService', '$uibModal', '$http', '$scope', '$filter'];

export default featureRequestController;