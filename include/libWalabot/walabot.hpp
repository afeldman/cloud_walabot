/*\file walabot.hpp
 *\author Anton Feldmann
 *\version 0.1.0
 *\date 05.09.2016
 */
#pragma once

#include <array>
#include <WalabotAPI.h>

/*!\brief walabot Namespace
 *\namespace libWalabot
 */
namespace libWalabot{

  class WalabotTarget{
  public:
    explicit WalabotTarget(double x=0.0,
                  double y=0.0,
                  double z=0.0,
                  double ampl=0.0);
    virtual ~WalabotTarget(){}
  public:
    double x;
    double y;
    double z;
    double ampl;
  };

  class Walabot{
  public:
    Walabot();
    virtual ~Walabot();

    void runTargetFinder();

    WalabotTarget &getTarget(int i);
    WalabotTarget &getTargets();

  private:
    void init();

  private:
    WALABOT_RESULT walabot_result;
    APP_STATUS walabot_status;

    double calibrationProcess;

    bool connected;
    bool mtimode;

    std::array<WalabotTarget,10> m_walabotTargets;
  };

}
