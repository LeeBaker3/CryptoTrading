/*
 * Author: Lee Baker.
 * Date: 2018-04-28
 * Version: 1.0
 * Summary: Creates the base Crypto Trading Database tables.
 */

-- Delete all database tables.
DROP TABLE IF EXISTS Price_action_tbl;
DROP TABLE IF EXISTS Coins_tbl;
DROP TABLE IF EXISTS Periods_tbl;
DROP TABLE IF EXISTS Sources_tbl;
DROP TABLE IF EXISTS Source_types_tbl;

/*
 * The Source Types table describes the types of sources 
 * that the price action data comes from.
 */
CREATE TABLE IF NOT EXISTS Source_types_tbl (
    source_type TEXT NOT NULL PRIMARY KEY UNIQUE
    );
/*
 * The Sources table lists the sources
 * of price action data such as exchanges and websites
 */
CREATE TABLE IF NOT EXISTS Sources_tbl (
    source_name TEXT NOT NULL PRIMARY KEY UNIQUE,
    source_type TEXT,
    FOREIGN KEY(source_type) REFERENCES Source_types_tbl(source_type)
    ); 

/*
 * The Coins tables list the various crypto coins and
 * tokens.
 */
CREATE TABLE IF NOT EXISTS Coins_tbl (
    coin TEXT NOT NULL PRIMARY KEY UNIQUE,
    coin_name TEXT, 
    coin_symbol TEXT
    );

/*
 * The Periods table list the various time periods that
 * are used to evaluate price action.
 */
CREATE TABLE IF NOT EXISTS Periods_tbl (
    period_name TEXT NOT NULL PRIMARY KEY UNIQUE,
    period_seconds INTEGER
    );

/*
 * The Price Action table list the price action of the coins and tokens
 * from the various sources for various time periods. Price action includes
 * the open, close, high, and low price for that time period and source.
 */
CREATE TABLE IF NOT EXISTS Price_actions_tbl (
    price_action_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    coin TEXT,
    price_action_open REAL,
    price_action_close REAL,
    price_action_high REAL,
    price_action_low REAL,
    price_action_volume REAL,
    period_start_time_utc TEXT,
    period_end_time_utc TEXT,
    period_start_time_unix INT,
    period_end_time_unix INT,
    period_name TEXT,
    source_name TEXT,
    FOREIGN KEY(coin) REFERENCES Coins_tbl(coin),
    FOREIGN KEY(period_name) REFERENCES Periods_tbl(period_name),
    FOREIGN KEY(source_name) REFERENCES Sources_tbl(source_name)
    );
