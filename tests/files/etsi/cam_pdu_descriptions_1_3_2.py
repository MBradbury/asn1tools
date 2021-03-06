EXPECTED = {'CAM-PDU-Descriptions': {'extensibility-implied': False,
                          'imports': {'ITS-Container': ['AccelerationControl',
                                                        'CauseCode',
                                                        'CenDsrcTollingZone',
                                                        'ClosedLanes',
                                                        'Curvature',
                                                        'CurvatureCalculationMode',
                                                        'DangerousGoodsBasic',
                                                        'DriveDirection',
                                                        'EmbarkationStatus',
                                                        'EmergencyPriority',
                                                        'ExteriorLights',
                                                        'Heading',
                                                        'ItsPduHeader',
                                                        'LanePosition',
                                                        'LateralAcceleration',
                                                        'Latitude',
                                                        'LightBarSirenInUse',
                                                        'Longitude',
                                                        'LongitudinalAcceleration',
                                                        'PathHistory',
                                                        'PerformanceClass',
                                                        'ProtectedCommunicationZone',
                                                        'ProtectedCommunicationZonesRSU',
                                                        'PtActivation',
                                                        'ReferencePosition',
                                                        'RoadworksSubCauseCode',
                                                        'SpecialTransportType',
                                                        'Speed',
                                                        'SpeedLimit',
                                                        'StationType',
                                                        'SteeringWheelAngle',
                                                        'TrafficRule',
                                                        'VehicleLength',
                                                        'VehicleRole',
                                                        'VehicleWidth',
                                                        'VerticalAcceleration',
                                                        'YawRate']},
                          'object-classes': {},
                          'object-sets': {},
                          'tags': 'AUTOMATIC',
                          'types': {'BasicContainer': {'members': [{'name': 'stationType',
                                                                    'type': 'StationType'},
                                                                   {'name': 'referencePosition',
                                                                    'type': 'ReferencePosition'},
                                                                   None],
                                                       'type': 'SEQUENCE'},
                                    'BasicVehicleContainerHighFrequency': {'members': [{'name': 'heading',
                                                                                        'type': 'Heading'},
                                                                                       {'name': 'speed',
                                                                                        'type': 'Speed'},
                                                                                       {'name': 'driveDirection',
                                                                                        'type': 'DriveDirection'},
                                                                                       {'name': 'vehicleLength',
                                                                                        'type': 'VehicleLength'},
                                                                                       {'name': 'vehicleWidth',
                                                                                        'type': 'VehicleWidth'},
                                                                                       {'name': 'longitudinalAcceleration',
                                                                                        'type': 'LongitudinalAcceleration'},
                                                                                       {'name': 'curvature',
                                                                                        'type': 'Curvature'},
                                                                                       {'name': 'curvatureCalculationMode',
                                                                                        'type': 'CurvatureCalculationMode'},
                                                                                       {'name': 'yawRate',
                                                                                        'type': 'YawRate'},
                                                                                       {'name': 'accelerationControl',
                                                                                        'optional': True,
                                                                                        'type': 'AccelerationControl'},
                                                                                       {'name': 'lanePosition',
                                                                                        'optional': True,
                                                                                        'type': 'LanePosition'},
                                                                                       {'name': 'steeringWheelAngle',
                                                                                        'optional': True,
                                                                                        'type': 'SteeringWheelAngle'},
                                                                                       {'name': 'lateralAcceleration',
                                                                                        'optional': True,
                                                                                        'type': 'LateralAcceleration'},
                                                                                       {'name': 'verticalAcceleration',
                                                                                        'optional': True,
                                                                                        'type': 'VerticalAcceleration'},
                                                                                       {'name': 'performanceClass',
                                                                                        'optional': True,
                                                                                        'type': 'PerformanceClass'},
                                                                                       {'name': 'cenDsrcTollingZone',
                                                                                        'optional': True,
                                                                                        'type': 'CenDsrcTollingZone'}],
                                                                           'type': 'SEQUENCE'},
                                    'BasicVehicleContainerLowFrequency': {'members': [{'name': 'vehicleRole',
                                                                                       'type': 'VehicleRole'},
                                                                                      {'name': 'exteriorLights',
                                                                                       'type': 'ExteriorLights'},
                                                                                      {'name': 'pathHistory',
                                                                                       'type': 'PathHistory'}],
                                                                          'type': 'SEQUENCE'},
                                    'CAM': {'members': [{'name': 'header',
                                                         'type': 'ItsPduHeader'},
                                                        {'name': 'cam',
                                                         'type': 'CoopAwareness'}],
                                            'type': 'SEQUENCE'},
                                    'CamParameters': {'members': [{'name': 'basicContainer',
                                                                   'type': 'BasicContainer'},
                                                                  {'name': 'highFrequencyContainer',
                                                                   'type': 'HighFrequencyContainer'},
                                                                  {'name': 'lowFrequencyContainer',
                                                                   'optional': True,
                                                                   'type': 'LowFrequencyContainer'},
                                                                  {'name': 'specialVehicleContainer',
                                                                   'optional': True,
                                                                   'type': 'SpecialVehicleContainer'},
                                                                  None],
                                                      'type': 'SEQUENCE'},
                                    'CoopAwareness': {'members': [{'name': 'generationDeltaTime',
                                                                   'type': 'GenerationDeltaTime'},
                                                                  {'name': 'camParameters',
                                                                   'type': 'CamParameters'}],
                                                      'type': 'SEQUENCE'},
                                    'DangerousGoodsContainer': {'members': [{'name': 'dangerousGoodsBasic',
                                                                             'type': 'DangerousGoodsBasic'}],
                                                                'type': 'SEQUENCE'},
                                    'EmergencyContainer': {'members': [{'name': 'lightBarSirenInUse',
                                                                        'type': 'LightBarSirenInUse'},
                                                                       {'name': 'incidentIndication',
                                                                        'optional': True,
                                                                        'type': 'CauseCode'},
                                                                       {'name': 'emergencyPriority',
                                                                        'optional': True,
                                                                        'type': 'EmergencyPriority'}],
                                                           'type': 'SEQUENCE'},
                                    'GenerationDeltaTime': {'named-numbers': {'oneMilliSec': 1},
                                                            'restricted-to': [(0,
                                                                               65535)],
                                                            'type': 'INTEGER'},
                                    'HighFrequencyContainer': {'members': [{'name': 'basicVehicleContainerHighFrequency',
                                                                            'type': 'BasicVehicleContainerHighFrequency'},
                                                                           {'name': 'rsuContainerHighFrequency',
                                                                            'type': 'RSUContainerHighFrequency'},
                                                                           None],
                                                               'type': 'CHOICE'},
                                    'LowFrequencyContainer': {'members': [{'name': 'basicVehicleContainerLowFrequency',
                                                                           'type': 'BasicVehicleContainerLowFrequency'},
                                                                          None],
                                                              'type': 'CHOICE'},
                                    'PublicTransportContainer': {'members': [{'name': 'embarkationStatus',
                                                                              'type': 'EmbarkationStatus'},
                                                                             {'name': 'ptActivation',
                                                                              'optional': True,
                                                                              'type': 'PtActivation'}],
                                                                 'type': 'SEQUENCE'},
                                    'RSUContainerHighFrequency': {'members': [{'name': 'protectedCommunicationZonesRSU',
                                                                               'optional': True,
                                                                               'type': 'ProtectedCommunicationZonesRSU'},
                                                                              None],
                                                                  'type': 'SEQUENCE'},
                                    'RescueContainer': {'members': [{'name': 'lightBarSirenInUse',
                                                                     'type': 'LightBarSirenInUse'}],
                                                        'type': 'SEQUENCE'},
                                    'RoadWorksContainerBasic': {'members': [{'name': 'roadworksSubCauseCode',
                                                                             'optional': True,
                                                                             'type': 'RoadworksSubCauseCode'},
                                                                            {'name': 'lightBarSirenInUse',
                                                                             'type': 'LightBarSirenInUse'},
                                                                            {'name': 'closedLanes',
                                                                             'optional': True,
                                                                             'type': 'ClosedLanes'}],
                                                                'type': 'SEQUENCE'},
                                    'SafetyCarContainer': {'members': [{'name': 'lightBarSirenInUse',
                                                                        'type': 'LightBarSirenInUse'},
                                                                       {'name': 'incidentIndication',
                                                                        'optional': True,
                                                                        'type': 'CauseCode'},
                                                                       {'name': 'trafficRule',
                                                                        'optional': True,
                                                                        'type': 'TrafficRule'},
                                                                       {'name': 'speedLimit',
                                                                        'optional': True,
                                                                        'type': 'SpeedLimit'}],
                                                           'type': 'SEQUENCE'},
                                    'SpecialTransportContainer': {'members': [{'name': 'specialTransportType',
                                                                               'type': 'SpecialTransportType'},
                                                                              {'name': 'lightBarSirenInUse',
                                                                               'type': 'LightBarSirenInUse'}],
                                                                  'type': 'SEQUENCE'},
                                    'SpecialVehicleContainer': {'members': [{'name': 'publicTransportContainer',
                                                                             'type': 'PublicTransportContainer'},
                                                                            {'name': 'specialTransportContainer',
                                                                             'type': 'SpecialTransportContainer'},
                                                                            {'name': 'dangerousGoodsContainer',
                                                                             'type': 'DangerousGoodsContainer'},
                                                                            {'name': 'roadWorksContainerBasic',
                                                                             'type': 'RoadWorksContainerBasic'},
                                                                            {'name': 'rescueContainer',
                                                                             'type': 'RescueContainer'},
                                                                            {'name': 'emergencyContainer',
                                                                             'type': 'EmergencyContainer'},
                                                                            {'name': 'safetyCarContainer',
                                                                             'type': 'SafetyCarContainer'},
                                                                            None],
                                                                'type': 'CHOICE'}},
                          'values': {}}}