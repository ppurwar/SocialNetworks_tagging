/****************************************************************************
 *
 * OpenBeacon.org - OnAir protocol specification and definition
 *
 * Copyright 2013 Milosch Meriac <meriac@openbeacon.de>
 *
 ****************************************************************************

 This file is part of the OpenBeacon.org active RFID firmware

 OpenBeacon is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 OpenBeacon is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

*/

#ifndef __OPENBEACON_PROTO_H__
#define __OPENBEACON_PROTO_H__

#define BEACONLOG_SIGHTING 0x01

#define CONFIG_TRACKER_CHANNEL 81
#define CONFIG_PROX_CHANNEL 76

#define CONFIG_SIGNATURE_SIZE 5
#define CONFIG_SIGHTING_SLOTS 3

#define RFBPROTO_BEACON_NG_SIGHTING 30
#define RFBPROTO_BEACON_NG_STATUS   31
#define RFBPROTO_BEACON_NG_PROX     32
#define RFBPROTO_BEACON_NG_MARKER   33

typedef struct
{
	int16_t rx_loss;
	int16_t tx_loss;
	int16_t px_power;
	uint16_t ticks;
} PACKED TBeaconNgStatus;

typedef struct
{
	int8_t rx_power;
	uint32_t uid;
} PACKED TBeaconNgSighting;

typedef union
{
	TBeaconNgStatus status;
	TBeaconNgSighting sighting[CONFIG_SIGHTING_SLOTS];
	uint8_t raw[15];
} PACKED TBeaconNgPayload;

typedef struct
{
	uint8_t proto;
	int8_t tx_power;
	int8_t angle;
	uint8_t voltage;
	uint32_t uid;
	uint32_t epoch;
	TBeaconNgPayload p;
 	uint8_t signature[CONFIG_SIGNATURE_SIZE];
} PACKED TBeaconNgTracker;

typedef struct
{
	uint8_t proto;
	int8_t tx_power;
	uint32_t uid;
	uint32_t counter;
	uint8_t voltage;
 	uint8_t signature[CONFIG_SIGNATURE_SIZE];
} PACKED TBeaconNgMarker;


typedef struct
{
	uint32_t uid;
	uint32_t epoch;
	uint16_t ticks;
} PACKED TBeaconNgProxAnnounce;

typedef union
{
	TBeaconNgProxAnnounce prox;
	uint8_t raw[10];
} PACKED TBeaconNgProxPayload;

typedef struct
{
	TBeaconNgProxPayload p;
	uint8_t proto;
	uint8_t signature[CONFIG_SIGNATURE_SIZE];
} PACKED TBeaconNgProx;

typedef struct
{
	uint16_t icrc16;
	uint8_t protocol;
	uint8_t interface;
	uint16_t reader_id;
	uint16_t size;
} PACKED TBeaconNetworkHdr;

/* BEACONLOG_SIGHTING */
typedef struct
{
	TBeaconNetworkHdr hdr;
	uint32_t sequence;
	uint32_t timestamp;
	TBeaconNgTracker log;
} PACKED TBeaconLogSighting;

#endif/*__OPENBEACON_PROTO_H__*/
