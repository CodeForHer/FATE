package com.webank.ai.fate.core.utils;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Properties;

import com.webank.ai.fate.core.result.StatusCode;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class Configuration {
    private static final Logger LOGGER = LogManager.getLogger();
    private final String confPath;
    private static Properties properties;

    public Configuration(String confPath){
        this.confPath = confPath;
    }

    public int load(){
        try{
            properties = new Properties();
            properties.load(new FileInputStream(this.confPath));
            return StatusCode.OK;
        }
        catch (FileNotFoundException ex){
            LOGGER.error("Can not found this file: {}", this.confPath);
            return StatusCode.NOFILE;
        }
        catch (Exception ex){
            LOGGER.error(ex);
            return StatusCode.UNKNOWNERROR;
        }
    }

    public static Properties getProperties() {
        return properties;
    }

    public static String getProperty(String key){
        return properties.getProperty(key);
    }
}