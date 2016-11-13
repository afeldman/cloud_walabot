/*\file walabot.hpp
 *\author Anton Feldmann
 *\version 0.1.0
 *\date 07.10.2016
 */
#pragma once

#include <array>
#include <memory>
#include <mutex>
using namespace std;

#include <cstdint>
#include <WalabotAPI.h>

#define CHECK_WALABOT_RESULT(result, func_name)                       \
  {                                                                   \
    if (result != WALABOT_SUCCESS){                                   \
      uint32_t extended = (uint32_t)Walabot_GetExtendedError();       \
      const uint8_t* errorStr = (uint8_t)Walabot_GetErrorString();    \
      std::cout << std::endl << "Error at " __FILE__ << ":"           \
      << std::dec << __LINE__ << " - "                                \
      << func_name << " result is 0x" << std::hex                     \
      << result << std::endl;                                         \
                                                                      \
      std::cout << "Error string: " << errorStr << std::endl;         \
                                                                      \
      std::cout << "Extended error: 0x" << std::hex                   \
      << extended << std::endl << std::endl;                          \
                                                                      \
      std::cout << "Press enter to continue ...";                     \
      std::string dummy;                                              \
      std::getline(std::cin, dummy);                                  \
      return;                                                         \
    }                                                                 \
  }

namespace Walabot{

  class Area{
  public:
    Area();
    explicit Area(double min_radialdistance,
                  double max_radialdistance,
                  double resolution_radialdistance,
                  double min_altitude,
                  double max_altitude,
                  double resolutionn_altitude,
                  double min_azimuth,
                  double max_azimuth,
                  double resolution_azimuth);
    virtual ~Area();

    array<double,3>& radialDistance(void);
    array<double,3>& altitude(void);
    array<double,3>& azimuth(void);

    void setRadialDistance(double min,
                           double max,
                           double res);
    void setAltitude(double min,
                     double max,
                     double res);
    void setAzimuth(double min,
                    double max,
                    double res);
  private:
    array<double,3> radialDistance;
    array<double,3> altitude;
    array<double,3> azimuth;

    mutex m_lock;
  };



}
