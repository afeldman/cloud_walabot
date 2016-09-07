/*\file sensortarget.hpp
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

class WalabotTarget : public std::iterator<std::forward_iterator_tag, SensorTarget>{

  SensorTarget* m_st;
public:
  WalabotTarget(SensorTarget* st) :m_st(st) {}
  WalabotTarget(const WalabotTarget& wal) : m_st(wal.m_st) {}
  WalabotTarget& operator++() {
++m_st;
return *this;}

  WalabotTarget operator++(int) {MyIterator tmp(*this); operator++(); return tmp;}
  bool operator==(const MyIterator& rhs) {return p==rhs.p;}
  bool operator!=(const MyIterator& rhs) {return p!=rhs.p;}
  int& operator*() {return *p;}

  };



}
