# CMake generated Testfile for 
# Source directory: /home/sasanka/ChargedUpCv/dependencies/opencv-4.x/modules/ml
# Build directory: /home/sasanka/ChargedUpCv/build/modules/ml
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(opencv_test_ml "/home/sasanka/ChargedUpCv/build/bin/opencv_test_ml" "--gtest_output=xml:opencv_test_ml.xml")
set_tests_properties(opencv_test_ml PROPERTIES  LABELS "Main;opencv_ml;Accuracy" WORKING_DIRECTORY "/home/sasanka/ChargedUpCv/build/test-reports/accuracy" _BACKTRACE_TRIPLES "/home/sasanka/ChargedUpCv/dependencies/opencv-4.x/cmake/OpenCVUtils.cmake;1769;add_test;/home/sasanka/ChargedUpCv/dependencies/opencv-4.x/cmake/OpenCVModule.cmake;1375;ocv_add_test_from_target;/home/sasanka/ChargedUpCv/dependencies/opencv-4.x/cmake/OpenCVModule.cmake;1133;ocv_add_accuracy_tests;/home/sasanka/ChargedUpCv/dependencies/opencv-4.x/modules/ml/CMakeLists.txt;2;ocv_define_module;/home/sasanka/ChargedUpCv/dependencies/opencv-4.x/modules/ml/CMakeLists.txt;0;")
