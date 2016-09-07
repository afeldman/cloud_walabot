/*\file walabotiterator.hpp
 *\author Anton Feldmann
 *\version 0.1.0
 *\date 05.09.2016
 */
#pragma once

#include <iterator>
using namespace std;

#include <WalabotAPI.h>

/*!\brief walabot Namespace
 *\namespace libWalabot
 */
namespace libWalabot{

  template<typename walabot, typename value_handle>
  class WalabotIteartor : public iterator<forward_iterator_tag, SensorTarget>{
  public:

    virtual WalabotIteartor& operator++();
    virtual WalabotIteartor operator++(int);
    virtual WalabotIteartor& operator--();
    virtual WalabotIteartor operator--(int);
    virtual bool operator==(const WalabotIteator& rhs);
    virtual bool operator!=(const WalabotIteator& rhs);
    reference operator*();
    pointer operator->();
  public:
    typedef const walabot_struct* walabot_ptr;
    typedef const walabot_struct& walabot_ref;
    typedef const value_handle&               reference;
    typedef const value_handle*               pointer;
  private:

  };
}
