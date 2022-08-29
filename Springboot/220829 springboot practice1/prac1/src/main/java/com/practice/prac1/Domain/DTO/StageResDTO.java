package com.practice.prac1.Domain.DTO;

import com.practice.prac1.Domain.Stage;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.util.Optional;

@Getter
@Builder
public class StageResDTO {
    private Long id;
    private String title;

    private String content;

    private Integer level;

}
