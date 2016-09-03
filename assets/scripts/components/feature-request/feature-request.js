import angular from "angular";

import templateUrl from './feature-request.html';
import featureRequestController from  "./featureRequestController";
import FeatureRequestApiService from "../../service/FeatureRequestApiService";

const featureRequestDetails = {
    templateUrl,
    controller: 'featureRequestController'
};

const component = angular.module('feature-request.components', [])
                .component('featureRequestDetails', featureRequestDetails)
                .controller('featureRequestController', featureRequestController)
                .service('FeatureRequestApiService', FeatureRequestApiService)
                .name;

export default component;
