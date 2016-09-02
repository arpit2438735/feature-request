import angular from "angular";

import templateUrl from './feature-request.html';
import featureRequestController from  "./featureRequestController";

const featureRequestDetails = {
    templateUrl,
    controller: 'featureRequestController'
};

const component = angular.module('feature-request.components', [])
                .component('featureRequestDetails', featureRequestDetails)
                .controller('featureRequestController', featureRequestController)
                .name;

export default component;
