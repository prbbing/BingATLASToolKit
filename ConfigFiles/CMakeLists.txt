# Set the minimum required CMake version:
cmake_minimum_required( VERSION 3.17 FATAL_ERROR )
project(WorkDir VERSION 1.0)
find_package( Athena 22.0 REQUIRED )

# Set up CTest:
atlas_ctest_setup()

# # Set up a work directory project:
atlas_project( WorkDir 1.0 USE Athena ${Athena_VERSION} )

# Set up the runtime environment setup script(s):
lcg_generate_env( SH_FILE ${CMAKE_BINARY_DIR}/${ATLAS_PLATFORM}/env_setup.sh )
install( FILES ${CMAKE_BINARY_DIR}/${ATLAS_PLATFORM}/env_setup.sh
   DESTINATION . )

# Set up CPack:
atlas_cpack_setup()
