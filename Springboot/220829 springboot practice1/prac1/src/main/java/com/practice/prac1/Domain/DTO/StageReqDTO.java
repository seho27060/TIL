package com.practice.prac1.Domain.DTO;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@AllArgsConstructor
@NoArgsConstructor
public class StageReqDTO {
    private String title;
    private String content;
    private Integer level;
}
